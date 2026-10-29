"""Self-improvement loop: evaluate on train, diagnose, propose a change, accept or reject it.

    python -m clausesearch.loop

Starts from configs/baseline.yaml. Each iteration diagnoses the current config's
train failures, takes the first rule whose trigger fires, evaluates the changed
config on train, and keeps it only if experiments/objective.yaml says so. Every
iteration, accepted or rejected, is appended to experiments/log.jsonl, and the
best config is written to configs/final.yaml. Test queries are dropped before
anything runs.
"""

import copy
import json
import random
import time
from datetime import datetime
from statistics import median

import yaml

from clausesearch.data import load
from clausesearch.evaluate import REPO, evaluate, load_unanswerable, save_run
from clausesearch.retrieve import Pipeline, load_config

OBJECTIVE = REPO / "experiments" / "objective.yaml"
LOG = REPO / "experiments" / "log.jsonl"
ITERATION_CONFIGS = REPO / "experiments" / "configs"
BASELINE = REPO / "configs" / "baseline.yaml"
FINAL = REPO / "configs" / "final.yaml"
MAX_ITERATIONS = 10


# ---------- measuring ----------

def run(config, corpus, queries, unanswerable):
    pipeline = Pipeline(config, corpus)
    start = time.perf_counter()
    result = evaluate(pipeline, queries, unanswerable, "train", config_name=config["name"])
    result["summary"]["seconds_per_query"] = (time.perf_counter() - start) / (len(queries) + len(unanswerable))
    return pipeline, result


def metrics(result):
    s = result["summary"]
    r = s["retrieval_only"]
    return {
        "budget_recall_2000": r["budget_recall"][2000],
        "budget_recall_500": r["budget_recall"][500],
        "recall@8": r["recall"][8],
        "recall@64": r["recall"][64],
        "precision@8": r["precision"][8],
        "false_abstain_rate": s["false_abstain_rate"],
        "correct_abstain_rate": s["correct_abstain_rate"],
        "seconds_per_query": s["seconds_per_query"],
    }


def bootstrap_win_rate(before, after, resamples, seed=0):
    """Share of paired resamples of queries in which `after` has the higher mean."""
    rng = random.Random(seed)
    diffs = [b - a for a, b in zip(before, after)]
    n = len(diffs)
    wins = sum(sum(diffs[rng.randrange(n)] for _ in range(n)) > 0 for _ in range(resamples))
    return wins / resamples


def decide(current, candidate, win_rate, kind, objective):
    """Apply the declared objective. Returns (accepted, list of reasons)."""
    g, a = objective["guardrails"], objective["acceptance"]
    reasons = []
    if candidate["false_abstain_rate"] > g["max_false_abstain_rate"]:
        reasons.append(f"false abstention {candidate['false_abstain_rate']:.3f} > {g['max_false_abstain_rate']}")
    if candidate["correct_abstain_rate"] < current["correct_abstain_rate"] - g["max_correct_abstain_drop"]:
        reasons.append("correct abstention dropped more than allowed")
    if candidate["budget_recall_500"] < current["budget_recall_500"] - g["max_budget_recall_500_drop"]:
        reasons.append("recall@500 chars dropped more than allowed")
    if candidate["seconds_per_query"] > g["max_seconds_per_query"]:
        reasons.append(f"{candidate['seconds_per_query']:.2f} s per query is too slow")

    gain = candidate["budget_recall_2000"] - current["budget_recall_2000"]
    if kind == "calibration":
        abstain_gain = candidate["correct_abstain_rate"] - current["correct_abstain_rate"]
        if abstain_gain < objective["calibration"]["min_correct_abstain_gain"]:
            reasons.append(f"correct abstention gain {abstain_gain:+.3f} is below the minimum")
        if gain < 0:
            reasons.append("primary metric fell")
    else:
        if gain < a["min_gain"]:
            reasons.append(f"primary gain {gain:+.3f} is below the minimum {a['min_gain']}")
        if win_rate < a["bootstrap_win_rate"]:
            reasons.append(f"bootstrap win rate {win_rate:.2f} is below {a['bootstrap_win_rate']}")
    return not reasons, reasons


# ---------- diagnosing ----------

def diagnose(result, queries):
    answerable = [r for r in result["rows"] if r["answerable"]]
    n = len(answerable)
    labels = {}
    for r in result["rows"]:
        labels[r["label"]] = labels.get(r["label"], 0) + 1
    return {
        "labels": labels,
        "n_answerable": n,
        "share": {k: labels.get(k, 0) / n for k in ("wrong_document", "wrong_section", "partial_span", "hit")},
        "not_in_top64": sum(r["first_hit_rank"] is None for r in answerable) / n,
        "not_in_top8": sum(r["first_hit_rank"] is None or r["first_hit_rank"] > 8 for r in answerable) / n,
        "false_answers": labels.get("false_answer", 0),
        "median_gold_chars": median(s["span"][1] - s["span"][0] for q in queries for s in q["snippets"]),
    }


# ---------- proposing: rules keyed on the diagnosis, tried in order ----------
# Each returns (change, reason, kind) or None when its trigger does not fire.

def rule_route_by_title(config, d, _):
    if config.get("route_by_title") or d["share"]["wrong_section"] < 0.3:
        return None
    return ({"route_by_title": True},
            f"{d['share']['wrong_section']:.0%} of answerable queries reach the right contract but the wrong "
            "section; the error report shows title and signature chunks ranking first because they repeat "
            "the contract-name prefix. Route on the prefix, rank passages with the question only.", "retrieval")


def rule_stem(config, d, _):
    # Run 1 triggered on "not in top 64", which routing made rare; ranking too low is the symptom.
    if config.get("stem") or d["not_in_top8"] < 0.2:
        return None
    return ({"stem": True},
            f"{d['not_in_top8']:.0%} of answerable queries have no relevant passage in the top 8; the error "
            "report shows word-form mismatches (query 'expiration', clause 'expire'). Stem all tokens.",
            "retrieval")


def rule_smaller_chunks(config, d, _):
    size = config["chunking"]["size"]
    if size <= 250 or d["median_gold_chars"] > 0.75 * size:
        return None
    return ({"chunking": {"size": size // 2, "overlap": 0}},
            f"median gold span is {d['median_gold_chars']:.0f} chars, so {size}-char chunks spend much of the "
            "reading budget on text around the answer. Halve the chunk size.", "retrieval")


def rule_overlap(config, d, _):
    chunking = config["chunking"]
    if chunking.get("overlap", 0) or d["share"]["partial_span"] < 0.05:
        return None
    return ({"chunking": {**chunking, "overlap": chunking["size"] // 2}},
            f"{d['share']['partial_span']:.0%} of answerable queries cover the answer only partly, consistent "
            "with clauses cut at chunk boundaries. Overlap chunks by half.", "retrieval")


def rule_larger_chunks(config, d, _):
    size = config["chunking"]["size"]
    if size >= 1000 or d["share"]["partial_span"] < 0.1:
        return None
    return ({"chunking": {"size": size * 2, "overlap": 0}},
            f"{d['share']['partial_span']:.0%} of answerable queries cover the answer only partly; "
            "longer chunks may keep whole clauses together. Double the chunk size.", "retrieval")


def rule_stopwords(config, d, _):
    if config.get("stopwords"):
        return None
    return ({"stopwords": True},
            "every question repeats template words ('is there', 'this contract', 'under') that carry no clause "
            "information but still add to BM25 scores. Drop them.", "retrieval")


def rule_calibrate_abstention(config, d, scores):
    """Parameter search: thresholds that maximise correct abstention within the false-abstention limit."""
    if not d["false_answers"]:
        return None
    best = scores["best"]
    limit = scores["max_false_abstain_rate"]
    route_options = sorted({0.0, *scores["route_unanswerable"], *scores["route_answerable"]}) if scores["routed"] else [0.0]
    score_options = sorted({0.0, *(s for s, _ in best)})
    choice = None
    for r in route_options:
        for t in score_options:
            def abstains(score, route):
                return score <= t or (route is not None and route < r)
            false_rate = sum(abstains(s, rt) for (s, rt) in scores["answerable"]) / len(scores["answerable"])
            if false_rate > limit:
                continue
            correct = sum(abstains(s, rt) for (s, rt) in scores["unanswerable"]) / len(scores["unanswerable"])
            key = (correct, -false_rate)
            if choice is None or key > choice[0]:
                choice = (key, r, t)
    if choice is None:
        return None
    (_, r, t) = choice
    return ({"abstain": {"min_score": round(t, 4), "route_min_score": round(r, 4)}},
            f"{d['false_answers']} unanswerable train queries still get an answer. Grid search on train over the "
            f"contract-match and passage-score thresholds for the most correct abstentions with false abstention "
            f"<= {limit}.", "calibration")


RULES = [rule_route_by_title, rule_stem, rule_smaller_chunks, rule_overlap,
         rule_larger_chunks, rule_stopwords, rule_calibrate_abstention]


def threshold_scores(pipeline, queries, unanswerable, objective):
    """Best passage score and contract-match score per train query, for threshold search."""
    def pairs(items):
        out = []
        for item in items:
            r = pipeline(item["query"])
            out.append((r["best_score"], r["route_score"]))
        return out

    answerable, unanswer = pairs(queries), pairs(unanswerable)
    return {
        "answerable": answerable,
        "unanswerable": unanswer,
        "best": answerable + unanswer,
        "routed": pipeline.route,
        "route_answerable": [rt for _, rt in answerable if rt is not None],
        "route_unanswerable": [rt for _, rt in unanswer if rt is not None],
        "max_false_abstain_rate": objective["guardrails"]["max_false_abstain_rate"],
    }


def merge(config, change):
    out = copy.deepcopy(config)
    for key, value in change.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = {**out[key], **value}
        else:
            out[key] = value
    return out


def canonical(config):
    return json.dumps({k: v for k, v in config.items() if k != "name"}, sort_keys=True)


# ---------- the loop ----------

def main():
    objective = yaml.safe_load(OBJECTIVE.read_text(encoding="utf-8"))
    queries, corpus = load()
    # Honesty: the loop only ever sees train.
    queries = [q for q in queries if q["split"] == "train"]
    unanswerable = [u for u in load_unanswerable() if u["split"] == "train"]
    resamples = objective["acceptance"]["bootstrap_resamples"]

    # Each loop run is appended under a new run number, so earlier runs stay in the log.
    previous = [json.loads(line) for line in LOG.read_text(encoding="utf-8").splitlines()] if LOG.exists() else []
    run_id = 1 + max((entry.get("run", 1) for entry in previous), default=0)

    current = load_config(BASELINE)
    pipeline, current_result = run(current, corpus, queries, unanswerable)
    current_metrics = metrics(current_result)
    log = [{
        "run": run_id, "iteration": 0, "time": datetime.now().isoformat(timespec="seconds"), "proposer": "human",
        "change": "baseline", "reason": "simplest reasonable pipeline", "config": current,
        "metrics": current_metrics, "decision": "baseline",
    }]
    print(f"iter 0 baseline: primary {current_metrics['budget_recall_2000']:.3f}")

    tried, fired = {canonical(current)}, set()
    for iteration in range(1, MAX_ITERATIONS + 1):
        diagnosis = diagnose(current_result, queries)
        scores = threshold_scores(pipeline, queries, unanswerable, objective)
        proposal = None
        for rule in RULES:
            if rule.__name__ in fired:
                continue
            out = rule(current, diagnosis, scores)
            if out and canonical(merge(current, out[0])) not in tried:
                proposal = (rule.__name__, *out)
                break
        if proposal is None:
            print("no rule fires any more; stopping")
            break

        rule_name, change, reason, kind = proposal
        fired.add(rule_name)
        candidate = merge(current, change)
        candidate["name"] = f"run{run_id}_iter{iteration:02d}"
        tried.add(canonical(candidate))
        cand_pipeline, cand_result = run(candidate, corpus, queries, unanswerable)
        cand_metrics = metrics(cand_result)

        before = [r["budget_recall"][2000] for r in current_result["rows"] if r["answerable"]]
        after = [r["budget_recall"][2000] for r in cand_result["rows"] if r["answerable"]]
        win_rate = bootstrap_win_rate(before, after, resamples)
        accepted, reasons = decide(current_metrics, cand_metrics, win_rate, kind, objective)

        ITERATION_CONFIGS.mkdir(parents=True, exist_ok=True)
        (ITERATION_CONFIGS / f"{candidate['name']}.yaml").write_text(
            yaml.safe_dump(candidate, sort_keys=False), encoding="utf-8")
        log.append({
            "run": run_id, "iteration": iteration, "time": datetime.now().isoformat(timespec="seconds"),
            "proposer": f"rule:{rule_name}", "kind": kind, "change": change, "reason": reason,
            "diagnosis": {"labels": diagnosis["labels"], "not_in_top64": round(diagnosis["not_in_top64"], 3)},
            "metrics_before": current_metrics, "metrics": cand_metrics, "bootstrap_win_rate": win_rate,
            "decision": "accepted" if accepted else "rejected", "rejection_reasons": reasons,
        })
        print(f"iter {iteration} {rule_name}: primary {current_metrics['budget_recall_2000']:.3f} -> "
              f"{cand_metrics['budget_recall_2000']:.3f}, correct abstain "
              f"{current_metrics['correct_abstain_rate']:.3f} -> {cand_metrics['correct_abstain_rate']:.3f}, "
              f"win {win_rate:.2f} -> {'ACCEPT' if accepted else 'reject: ' + '; '.join(reasons)}")
        if accepted:
            current, pipeline, current_result, current_metrics = candidate, cand_pipeline, cand_result, cand_metrics

    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.writelines(json.dumps(entry) + "\n" for entry in log)
    final = {**current, "name": "final"}
    FINAL.write_text(f"# Written by clausesearch.loop from {current['name']}.\n"
                     + yaml.safe_dump(final, sort_keys=False), encoding="utf-8")
    current_result["summary"]["config"] = "final"
    print(f"final = {current['name']}, primary {current_metrics['budget_recall_2000']:.3f}; "
          f"wrote {FINAL.relative_to(REPO)}, {LOG.relative_to(REPO)}, {save_run(current_result).relative_to(REPO)}")


if __name__ == "__main__":
    main()
