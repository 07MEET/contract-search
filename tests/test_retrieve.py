from clausesearch.retrieve import Pipeline, chunk_fixed

CONFIG = {"chunking": {"size": 40, "overlap": 0}, "top_k": 3, "abstain": {"min_score": 0.0}}
CORPUS = {
    "cuad/a.txt": "This Agreement shall be governed by the laws of the State of Delaware. " * 2,
    "cuad/b.txt": "Either party may terminate this Agreement upon thirty days written notice. " * 2,
    "cuad/c.txt": "The Supplier shall maintain insurance coverage of five million dollars. " * 2,
}


def test_chunks_cover_text_exactly():
    text = "x" * 1234
    spans = chunk_fixed(text, 500)
    assert spans == [(0, 500), (500, 1000), (1000, 1234)]
    assert "".join(text[s:e] for s, e in spans) == text


def test_overlapping_chunks_step_back():
    assert chunk_fixed("x" * 25, 10, overlap=5)[:3] == [(0, 10), (5, 15), (10, 20)]


def test_returns_ranked_passages_from_the_right_contract():
    pipeline = Pipeline(CONFIG, CORPUS)
    result = pipeline("Which state's laws govern this agreement? Delaware?")
    top = result["passages"][0]
    assert top["file_path"] == "cuad/a.txt"
    assert "Delaware" in pipeline.text(top) or "governed" in pipeline.text(top)
    assert [p["score"] for p in result["passages"]] == sorted((p["score"] for p in result["passages"]), reverse=True)
    assert not result["abstain"]


def test_abstains_when_nothing_matches():
    assert Pipeline(CONFIG, CORPUS)("zebra giraffe")["abstain"]
