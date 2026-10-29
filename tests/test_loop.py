from clausesearch.loop import bootstrap_win_rate, decide, merge

OBJECTIVE = {
    "acceptance": {"min_gain": 0.01, "bootstrap_resamples": 200, "bootstrap_win_rate": 0.9},
    "calibration": {"min_correct_abstain_gain": 0.05},
    "guardrails": {"max_false_abstain_rate": 0.10, "max_correct_abstain_drop": 0.05,
                   "max_budget_recall_500_drop": 0.02, "max_seconds_per_query": 1.0},
}
BASE = {"budget_recall_2000": 0.30, "budget_recall_500": 0.10, "false_abstain_rate": 0.0,
        "correct_abstain_rate": 0.0, "seconds_per_query": 0.01}


def test_bootstrap_win_rate():
    assert bootstrap_win_rate([0.1] * 20, [0.2] * 20, 200) == 1.0  # better on every query
    assert bootstrap_win_rate([0.2] * 20, [0.2] * 20, 200) == 0.0  # no difference never "wins"


def test_accepts_a_clear_gain():
    assert decide(BASE, {**BASE, "budget_recall_2000": 0.40}, 0.99, "retrieval", OBJECTIVE) == (True, [])


def test_rejects_small_or_noisy_gains():
    assert not decide(BASE, {**BASE, "budget_recall_2000": 0.305}, 0.99, "retrieval", OBJECTIVE)[0]
    assert not decide(BASE, {**BASE, "budget_recall_2000": 0.40}, 0.60, "retrieval", OBJECTIVE)[0]


def test_rejects_a_guardrail_violation():
    candidate = {**BASE, "budget_recall_2000": 0.40, "false_abstain_rate": 0.2}
    accepted, reasons = decide(BASE, candidate, 0.99, "retrieval", OBJECTIVE)
    assert not accepted and "false abstention" in reasons[0]


def test_calibration_is_judged_on_abstention():
    better_abstention = {**BASE, "correct_abstain_rate": 0.5, "false_abstain_rate": 0.05}
    assert decide(BASE, better_abstention, 0.0, "calibration", OBJECTIVE) == (True, [])


def test_merge_keeps_unchanged_nested_keys():
    config = {"chunking": {"size": 500, "overlap": 0}, "stem": False}
    assert merge(config, {"chunking": {"size": 250}}) == {"chunking": {"size": 250, "overlap": 0}, "stem": False}
