from clausesearch.retrieve import Pipeline, chunk_fixed, split_query, tokenize

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


def test_split_query():
    assert split_query("Consider the X Agreement; What is the governing law?") == (
        "Consider the X Agreement", "What is the governing law?")
    assert split_query("What is the governing law?") == ("", "What is the governing law?")


def test_stemming_matches_word_forms():
    assert tokenize("expiration expire expires", stem=True)[1:] == tokenize("expire expires", stem=True)
    assert tokenize("Is there a cap on liability", stopwords=True) == ["cap", "liability"]


def test_routing_searches_only_the_named_contract():
    corpus = {
        "cuad/acme.txt": "SUPPLY AGREEMENT between Acme Corp and Beta LLC. " + "filler text " * 20
                         + "This Agreement is governed by the laws of Texas.",
        "cuad/zeta.txt": "LICENSE AGREEMENT between Zeta Inc and Omega Ltd. " + "filler text " * 20
                         + "This Agreement is governed by the laws of Ohio.",
        # BM25 gives zero weight to a word found in half the documents, so use 3+ contracts.
        "cuad/kappa.txt": "SERVICE AGREEMENT between Kappa Co and Sigma plc. " + "filler text " * 20
                          + "This Agreement is governed by the laws of Utah.",
    }
    config = {**CONFIG, "chunking": {"size": 60, "overlap": 0}, "route_by_title": True}
    result = Pipeline(config, corpus)("Consider the License Agreement between Zeta Inc and Omega Ltd; What is the governing law?")
    assert {p["file_path"] for p in result["passages"]} == {"cuad/zeta.txt"}
    assert result["route_score"] > 0
