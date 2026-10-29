"""Chunk the contracts, index them, and answer queries with ranked passages.

Every pipeline choice comes from a config dict (loaded from configs/*.yaml),
so the improvement loop can change them without touching code. Options that a
config leaves out default to the baseline behaviour.
"""

import re
from bisect import bisect_right
from pathlib import Path

import snowballstemmer
import yaml
from rank_bm25 import BM25Okapi

STEMMER = snowballstemmer.stemmer("english")
# Words in almost every question template that say nothing about which clause is meant.
STOPWORDS = frozenset(
    "a an and any are as at be by can do does for from has have how in is it of on or "
    "that the there this to under what when which who with".split()
)
HEADER_CHARS = 2000  # the start of a contract (title, parties) that routing matches against


def load_config(path: str | Path) -> dict:
    config = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    config.setdefault("name", Path(path).stem)
    return config


def chunk_fixed(text: str, size: int, overlap: int = 0) -> list[tuple[int, int]]:
    """Fixed-size character windows over the text, as (start, end) spans."""
    step = size - overlap
    return [(i, min(i + size, len(text))) for i in range(0, len(text), step)]


def tokenize(text: str, stem: bool = False, stopwords: bool = False) -> list[str]:
    tokens = re.findall(r"\w+", text.lower())
    if stopwords:
        tokens = [t for t in tokens if t not in STOPWORDS]
    return STEMMER.stemWords(tokens) if stem else tokens


# A heading starts a line or follows a run of 3+ spaces: optional "Section"/"Article", an optional
# number (9, 5.1, 22, II), then a short title (optionally in brackets) ending in "." / ":" or the
# end of the line. Seen in the corpus: "9. Term and Renewal.", "22 JURISDICTION AND CHOICE OF LAW",
# "     7. NON-COMPETITION.", "ARTICLE II  DUTIES OF AGENT", "Section 9.11 [Governing Law]."
HEADING = re.compile(
    # Each part starts on a non-space character, so runs of spaces can only be matched one way
    # (overlapping optional space patterns made the regex engine backtrack for minutes).
    r"(?:^|(?<=\s{3}))(?=\S)\"?(?:(?:section|article) +)?"
    r"(?:(?P<num>\d+(?:\.\d+)*\.?|(?-i:[IVX]+)\.?) +)?"
    r"\[?(?P<title>[^\s.:\[\]][^.:\n\[\]]{2,59}?)\]?(?:[.:]|$)",
    re.MULTILINE | re.IGNORECASE,
)
SMALL_WORDS = frozenset("a an and as at by for in of on or the to with".split())
PREAMBLE_WORDS = frozenset("and between by exhibit now recitals therefore whereas witnesseth".split())


def _is_title(text: str) -> bool:
    words = text.split()
    return (1 <= len(words) <= 8 and any(w.lower() not in SMALL_WORDS for w in words)
            and all(w[0].isupper() or w.lower() in SMALL_WORDS for w in words))


def find_headings(text: str) -> list[tuple[int, str]]:
    """Section headings as (start offset, path), e.g. (812, "INTELLECTUAL PROPERTY / ISA's Intellectual Property").

    A lightweight stand-in for a table of contents (the idea behind STAIR, arXiv 2609.03874):
    numbered headings nest by their depth (5 > 5.1), unnumbered ALL-CAPS headings are top level.
    """
    headings, stack = [], []  # stack holds (depth, title) of the open sections
    for m in HEADING.finditer(text):
        number, title = m.group("num"), m.group("title").strip()
        at_line_start = m.start() == 0 or text[m.start() - 1] == "\n"
        if not _is_title(title) or all(w.lower() in PREAMBLE_WORDS for w in title.split()):
            continue
        # Unnumbered headings must be ALL CAPS on their own line; mid-line ones must be numbered.
        if not (number or (title.isupper() and at_line_start)) or not (number or at_line_start):
            continue
        depth = number.rstrip(".").count(".") + 1 if number and number[0].isdigit() else 1
        stack = [(d, t) for d, t in stack if d < depth] + [(depth, title)]
        headings.append((m.start(), " / ".join(t for _, t in stack)))
    return headings


def section_at(headings: list[tuple[int, str]], position: int) -> str:
    """Path of the section that contains `position` ('' before the first heading)."""
    i = bisect_right([pos for pos, _ in headings], position) - 1
    return headings[i][1] if i >= 0 else ""


def split_query(query: str) -> tuple[str, str]:
    """'Consider the <contract>; <question>' -> (contract description, question)."""
    if ";" in query:
        prefix, question = query.split(";", 1)
        return prefix.strip(), question.strip()
    return "", query.strip()


class Pipeline:
    """Callable as `pipeline(query) -> {"passages": [...], "abstain": bool, ...}`."""

    def __init__(self, config: dict, corpus: dict[str, str]):
        self.config = config
        self.corpus = corpus
        self.stem = config.get("stem", False)
        self.stopwords = config.get("stopwords", False)
        chunking = config["chunking"]
        self.chunks = [
            (file_path, span)
            for file_path, text in corpus.items()
            for span in chunk_fixed(text, chunking["size"], chunking.get("overlap", 0))
        ]
        # Section path of each chunk; indexed with the chunk when section_headings is on.
        # Only the indexed text changes: returned spans are still the chunk's own offsets.
        headings = {fp: find_headings(text) for fp, text in corpus.items()}
        self.sections = [section_at(headings[fp], s) for fp, (s, _) in self.chunks]
        with_headings = config.get("section_headings", False)
        self.bm25 = BM25Okapi([
            self._tok((self.sections[i] + "\n" if with_headings else "") + corpus[fp][s:e])
            for i, (fp, (s, e)) in enumerate(self.chunks)
        ])

        self.route = config.get("route_by_title", False)
        if self.route:
            self.files = list(corpus)
            self.chunks_of = {fp: [i for i, (f, _) in enumerate(self.chunks) if f == fp] for fp in self.files}
            # File names add the company and agreement type, e.g. "GluMobileInc ... Content License".
            headers = [re.sub(r"[_\W]+", " ", fp) + " " + corpus[fp][:HEADER_CHARS] for fp in self.files]
            self.router = BM25Okapi([self._tok(h) for h in headers])

    def _tok(self, text: str) -> list[str]:
        return tokenize(text, self.stem, self.stopwords)

    def __call__(self, query: str) -> dict:
        route_score = None
        candidates = range(len(self.chunks))
        search_text = query
        if self.route:
            # The contract description picks the contract; only the question ranks passages.
            prefix, search_text = split_query(query)
            route_scores = self.router.get_scores(self._tok(prefix)) if prefix else [0.0] * len(self.files)
            best_file = max(range(len(self.files)), key=lambda i: route_scores[i])
            route_score = float(route_scores[best_file])
            candidates = self.chunks_of[self.files[best_file]]

        scores = self.bm25.get_scores(self._tok(search_text))
        ranked = sorted(candidates, key=lambda i: -scores[i])[: self.config["top_k"]]
        passages = [
            {"file_path": self.chunks[i][0], "span": self.chunks[i][1], "score": float(scores[i]),
             "section": self.sections[i]}
            for i in ranked
        ]
        best_score = passages[0]["score"] if passages else 0.0
        abstain_cfg = self.config["abstain"]
        abstain = best_score <= abstain_cfg["min_score"] or (
            route_score is not None and route_score < abstain_cfg.get("route_min_score", 0.0)
        )
        return {"passages": passages, "abstain": abstain, "best_score": best_score, "route_score": route_score}

    def text(self, passage: dict) -> str:
        start, end = passage["span"]
        return self.corpus[passage["file_path"]][start:end]


def load_pipeline(config_path: str | Path) -> Pipeline:
    """Load the corpus and build the pipeline a config describes (used by the CLI and app)."""
    from clausesearch.data import load

    _, corpus = load()
    return Pipeline(load_config(config_path), corpus)
