"""Chunk the contracts, index them, and answer queries with ranked passages.

Every pipeline choice comes from a config dict (loaded from configs/*.yaml),
so the improvement loop can change them without touching code.
"""

import re
from pathlib import Path

import yaml
from rank_bm25 import BM25Okapi


def load_config(path: str | Path) -> dict:
    config = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    config.setdefault("name", Path(path).stem)
    return config


def chunk_fixed(text: str, size: int, overlap: int = 0) -> list[tuple[int, int]]:
    """Fixed-size character windows over the text, as (start, end) spans."""
    step = size - overlap
    return [(i, min(i + size, len(text))) for i in range(0, len(text), step)]


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


class Pipeline:
    """Callable as `pipeline(query) -> {"passages": [...], "abstain": bool}`."""

    def __init__(self, config: dict, corpus: dict[str, str]):
        self.config = config
        self.corpus = corpus
        chunking = config["chunking"]
        self.chunks = [
            (file_path, span)
            for file_path, text in corpus.items()
            for span in chunk_fixed(text, chunking["size"], chunking.get("overlap", 0))
        ]
        self.bm25 = BM25Okapi([tokenize(corpus[fp][s:e]) for fp, (s, e) in self.chunks])

    def __call__(self, query: str) -> dict:
        scores = self.bm25.get_scores(tokenize(query))
        ranked = sorted(range(len(scores)), key=lambda i: -scores[i])[: self.config["top_k"]]
        passages = [
            {"file_path": self.chunks[i][0], "span": self.chunks[i][1], "score": float(scores[i])}
            for i in ranked
        ]
        best = passages[0]["score"] if passages else 0.0
        return {"passages": passages, "abstain": best <= self.config["abstain"]["min_score"]}

    def text(self, passage: dict) -> str:
        start, end = passage["span"]
        return self.corpus[passage["file_path"]][start:end]


def load_pipeline(config_path: str | Path) -> Pipeline:
    """Load the corpus and build the pipeline a config describes (used by the CLI and app)."""
    from clausesearch.data import load

    _, corpus = load()
    return Pipeline(load_config(config_path), corpus)
