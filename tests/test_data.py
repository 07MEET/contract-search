import pytest

from clausesearch.data import DATA_DIR, assign_split, check_offsets, load

needs_data = pytest.mark.skipif(
    not (DATA_DIR / "benchmarks" / "cuad.json").exists(),
    reason="run scripts/download_data.py first",
)


@needs_data
def test_mini_selection_and_split():
    queries, corpus = load()  # load() also verifies every gold offset
    assert len(queries) == 194
    assert len(corpus) == 29
    assert sum(q["split"] == "test" for q in queries) == 54
    assert all(s["file_path"] in corpus for q in queries for s in q["snippets"])


def test_assign_split_ignores_surrounding_whitespace():
    q = "Consider the X agreement; What is the governing law for this contract?"
    assert assign_split(q) == assign_split(f"  {q}\n")
    assert assign_split(q) in {"train", "test"}


def test_check_offsets_catches_a_wrong_span():
    corpus = {"cuad/a.txt": "The governing law is Delaware."}
    good = [{"query": "q", "snippets": [{"file_path": "cuad/a.txt", "span": (21, 29), "answer": "Delaware"}]}]
    check_offsets(good, corpus)
    bad = [{"query": "q", "snippets": [{"file_path": "cuad/a.txt", "span": (20, 28), "answer": "Delaware"}]}]
    with pytest.raises(ValueError):
        check_offsets(bad, corpus)
