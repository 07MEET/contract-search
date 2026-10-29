from pytest import approx

from clausesearch.evaluate import clip_to_budget, diagnose, evaluate, precision_recall


def p(start, end, file_path="cuad/a.txt"):
    return {"file_path": file_path, "span": (start, end), "score": 1.0}


GOLD = [p(100, 500)]  # 400 gold characters


def test_exact_match_scores_one():
    assert precision_recall([p(100, 500)], GOLD) == (1.0, 1.0)


def test_partial_overlap():
    # 200 retrieved chars, 100 of them inside the 400-char gold span
    assert precision_recall([p(0, 200)], GOLD) == approx((0.5, 0.25))


def test_overlapping_passages_are_not_double_counted():
    # Two copies of the same text: still 400 retrieved chars, all relevant
    assert precision_recall([p(100, 500), p(100, 500)], GOLD) == (1.0, 1.0)
    # Overlapping halves merge to 100..500
    assert precision_recall([p(100, 400), p(300, 500)], GOLD) == (1.0, 1.0)


def test_right_offsets_wrong_file_scores_zero():
    assert precision_recall([p(100, 500, "cuad/b.txt")], GOLD) == (0.0, 0.0)


def test_nothing_retrieved_scores_zero():
    assert precision_recall([], GOLD) == (0.0, 0.0)


def test_budget_cuts_the_last_passage():
    clipped = clip_to_budget([p(0, 300), p(1000, 1500)], 400)
    assert [c["span"] for c in clipped] == [(0, 300), (1000, 1100)]


def test_diagnosis_labels():
    assert diagnose([p(100, 500)], GOLD, abstain=True) == "false_abstain"
    assert diagnose([p(100, 500, "cuad/b.txt")], GOLD, abstain=False) == "wrong_document"
    assert diagnose([p(600, 900)], GOLD, abstain=False) == "wrong_section"
    assert diagnose([p(100, 150)], GOLD, abstain=False) == "partial_span"
    assert diagnose([p(100, 400)], GOLD, abstain=False) == "hit"


def test_evaluate_scores_abstention_both_ways(tmp_path):
    queries = [
        {"query": "q1", "split": "test", "snippets": GOLD},
        {"query": "q2", "split": "test", "snippets": GOLD},
        {"query": "q-train", "split": "train", "snippets": GOLD},
    ]
    unanswerable = [
        {"query": "u1", "split": "test", "category": "off_topic"},
        {"query": "u2", "split": "test", "category": "off_topic"},
    ]
    # Finds q1 exactly, abstains on q2 and on u1, answers u2.
    outputs = {
        "q1": {"passages": [p(100, 500)], "abstain": False},
        "q2": {"passages": [p(100, 500)], "abstain": True},
        "u1": {"passages": [], "abstain": True},
        "u2": {"passages": [p(0, 50)], "abstain": False},
    }
    log = tmp_path / "test_runs.log"
    result = evaluate(outputs.__getitem__, queries, unanswerable, "test", config_name="toy", test_log=log)
    s = result["summary"]

    assert s["n_answerable"] == 2 and s["n_unanswerable"] == 2
    assert s["retrieval_only"]["recall"][1] == 1.0  # both ranked lists are perfect
    assert s["end_to_end"]["recall"][1] == 0.5      # the abstention on q2 costs it
    assert s["false_abstain_rate"] == 0.5
    assert s["correct_abstain_rate"] == 0.5
    assert s["labels"] == {"hit": 1, "false_abstain": 1, "correct_abstain": 1, "false_answer": 1}
    assert len(log.read_text(encoding="utf-8").splitlines()) == 1  # every test-split run is logged


def test_train_runs_are_not_logged(tmp_path):
    log = tmp_path / "test_runs.log"
    queries = [{"query": "q", "split": "train", "snippets": GOLD}]
    evaluate(lambda q: {"passages": [], "abstain": True}, queries, [], "train", test_log=log)
    assert not log.exists()
