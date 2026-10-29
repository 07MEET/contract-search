"""Load the LegalBench-RAG-mini CUAD queries and the contracts they refer to.

Run `python -m clausesearch.data` to print a summary of the data.
"""

import hashlib
import json
import random
import unicodedata
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def mini(tests, n=194):
    """The benchmark authors' LegalBench-RAG-mini selection, unchanged."""
    if len(tests) <= n:
        return tests

    def key(t):
        random.seed(t["snippets"][0]["file_path"])
        return random.random()

    return sorted(tests, key=key)[:n]


def assign_split(query: str) -> str:
    """The fixed train/test split from the brief, unchanged."""
    h = int(hashlib.sha256(query.strip().encode("utf-8")).hexdigest(), 16)
    return "test" if h % 10 < 3 else "train"


def nfc(path: str) -> str:
    # One CUAD file_path is NFD while its file name on disk is NFC.
    return unicodedata.normalize("NFC", path)


def load_queries(data_dir: Path = DATA_DIR) -> list[dict]:
    """The 194 mini queries, each with its split and gold snippets."""
    raw = (data_dir / "benchmarks" / "cuad.json").read_text(encoding="utf-8")
    tests = json.loads(raw)["tests"]
    return [
        {
            "query": t["query"],
            "split": assign_split(t["query"]),
            "snippets": [
                {"file_path": nfc(s["file_path"]), "span": tuple(s["span"]), "answer": s["answer"]}
                for s in t["snippets"]
            ],
        }
        for t in mini(tests)
    ]


def load_corpus(queries: list[dict], data_dir: Path = DATA_DIR) -> dict[str, str]:
    """Text of every contract the queries refer to, keyed by file_path ("cuad/<name>.txt")."""
    on_disk = {nfc(p.name): p for p in (data_dir / "corpus" / "cuad").glob("*.txt")}
    corpus = {}
    for file_path in sorted({s["file_path"] for q in queries for s in q["snippets"]}):
        # Default text mode (universal newlines) is what the gold offsets assume.
        corpus[file_path] = on_disk[file_path.split("/", 1)[1]].read_text(encoding="utf-8")
    return corpus


def check_offsets(queries: list[dict], corpus: dict[str, str]) -> None:
    """Raise if any gold span does not slice out exactly its answer text."""
    bad = [
        (q["query"], s["span"])
        for q in queries
        for s in q["snippets"]
        if corpus[s["file_path"]][s["span"][0] : s["span"][1]] != s["answer"]
    ]
    if bad:
        raise ValueError(f"{len(bad)} gold spans do not match their answer text, first: {bad[0]}")


def load(data_dir: Path = DATA_DIR) -> tuple[list[dict], dict[str, str]]:
    """Queries and corpus, with every gold offset verified."""
    queries = load_queries(data_dir)
    corpus = load_corpus(queries, data_dir)
    check_offsets(queries, corpus)
    return queries, corpus


if __name__ == "__main__":
    queries, corpus = load()
    splits = Counter(q["split"] for q in queries)
    n_snippets = sum(len(q["snippets"]) for q in queries)
    n_dupes = len(queries) - len({q["query"] for q in queries})
    print(f"queries: {len(queries)} (train {splits['train']}, test {splits['test']}), duplicates: {n_dupes}")
    print(f"contracts indexed: {len(corpus)}, characters: {sum(map(len, corpus.values())):,}")
    print(f"gold snippets: {n_snippets}, all offsets verified")
