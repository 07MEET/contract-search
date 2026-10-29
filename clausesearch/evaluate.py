"""Score a retrieval system on the benchmark queries and the unanswerable set.

A system is any function `system(query) -> {"passages": [...], "abstain": bool}`.
Passages are ranked best first, each `{"file_path", "span": (start, end), "score"}`,
and the ranked list is kept even when the system abstains so retrieval and
abstention can be scored separately. Return at least max(K_VALUES) passages
when the corpus has them. Gold spans are only read here, never passed to the system.
"""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import mean

REPO = Path(__file__).resolve().parent.parent
UNANSWERABLE_PATH = REPO / "eval" / "unanswerable.jsonl"
TEST_RUN_LOG = REPO / "experiments" / "test_runs.log"
RUNS_DIR = REPO / "runs"

K_VALUES = (1, 2, 4, 8, 16, 32, 64)
BUDGETS = (500, 1000, 2000, 4000)  # characters
HIT_RECALL = 0.5  # a query counts as a "hit" when at least half its gold text is covered


def load_unanswerable(path: Path = UNANSWERABLE_PATH) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def merge_spans(items: list[dict]) -> dict[str, list[tuple[int, int]]]:
    """Union of spans per file, sorted and non-overlapping, so no character counts twice."""
    by_file: dict[str, list[tuple[int, int]]] = {}
    for item in items:
        by_file.setdefault(item["file_path"], []).append(tuple(item["span"]))
    merged = {}
    for file_path, spans in by_file.items():
        out: list[tuple[int, int]] = []
        for start, end in sorted(spans):
            if out and start <= out[-1][1]:
                out[-1] = (out[-1][0], max(out[-1][1], end))
            else:
                out.append((start, end))
        merged[file_path] = out
    return merged


def _length(spans_by_file: dict) -> int:
    return sum(end - start for spans in spans_by_file.values() for start, end in spans)


def precision_recall(passages: list[dict], gold: list[dict]) -> tuple[float, float]:
    """Character-level precision and recall of the passages against the gold snippets."""
    retrieved = merge_spans(passages)
    gold_spans = merge_spans(gold)
    overlap = sum(
        max(0, min(e1, e2) - max(s1, s2))
        for file_path, spans in retrieved.items()
        for s1, e1 in spans
        for s2, e2 in gold_spans.get(file_path, [])
    )
    n_retrieved = _length(retrieved)
    return (overlap / n_retrieved if n_retrieved else 0.0), overlap / _length(gold_spans)


def clip_to_budget(passages: list[dict], budget: int) -> list[dict]:
    """Passages in rank order until `budget` characters are used, cutting the last one short."""
    out, left = [], budget
    for p in passages:
        if left <= 0:
            break
        start, end = p["span"]
        out.append({**p, "span": (start, min(end, start + left))})
        left -= end - start
    return out


def diagnose(passages: list[dict], gold: list[dict], abstain: bool) -> str:
    """Why an answerable query did or did not succeed within the passages given."""
    if abstain:
        return "false_abstain"
    gold_files = {g["file_path"] for g in gold}
    if not any(p["file_path"] in gold_files for p in passages):
        return "wrong_document"
    _, recall = precision_recall(passages, gold)
    if recall == 0:
        return "wrong_section"
    return "hit" if recall >= HIT_RECALL else "partial_span"


def first_hit_rank(passages: list[dict], gold: list[dict]) -> int | None:
    """1-based rank of the first passage that overlaps any gold text."""
    for rank, p in enumerate(passages, 1):
        if precision_recall([p], gold)[1] > 0:
            return rank
    return None


def evaluate(system, queries, unanswerable, split, label_k=8, config_name="unnamed", test_log=TEST_RUN_LOG):
    """Run `system` on one split and return summary metrics plus one row per query."""
    queries = [q for q in queries if q["split"] == split]
    unanswerable = [u for u in unanswerable if u["split"] == split]

    rows = []
    for q in queries:
        result = system(q["query"])
        passages, abstain, gold = result["passages"], result["abstain"], q["snippets"]
        pr = {k: precision_recall(passages[:k], gold) for k in K_VALUES}
        rows.append({
            "query": q["query"],
            "answerable": True,
            "abstain": abstain,
            "label": diagnose(passages[:label_k], gold, abstain),
            "first_hit_rank": first_hit_rank(passages, gold),
            "precision": {k: p for k, (p, _) in pr.items()},
            "recall": {k: r for k, (_, r) in pr.items()},
            "budget_recall": {b: precision_recall(clip_to_budget(passages, b), gold)[1] for b in BUDGETS},
        })
    for u in unanswerable:
        abstain = system(u["query"])["abstain"]
        rows.append({
            "query": u["query"],
            "answerable": False,
            "category": u["category"],
            "abstain": abstain,
            "label": "correct_abstain" if abstain else "false_answer",
        })

    answerable = [r for r in rows if r["answerable"]]
    unanswer = [r for r in rows if not r["answerable"]]

    def avg(metric, k, end_to_end):
        return mean(0.0 if end_to_end and r["abstain"] else r[metric][k] for r in answerable)

    summary = {
        "config": config_name,
        "split": split,
        "n_answerable": len(answerable),
        "n_unanswerable": len(unanswer),
        "label_k": label_k,
        "retrieval_only": {
            "precision": {k: avg("precision", k, False) for k in K_VALUES},
            "recall": {k: avg("recall", k, False) for k in K_VALUES},
            "budget_recall": {b: avg("budget_recall", b, False) for b in BUDGETS},
        },
        "end_to_end": {
            "precision": {k: avg("precision", k, True) for k in K_VALUES},
            "recall": {k: avg("recall", k, True) for k in K_VALUES},
        },
        "false_abstain_rate": mean(r["abstain"] for r in answerable),
        "correct_abstain_rate": mean(r["abstain"] for r in unanswer) if unanswer else None,
        "labels": dict(Counter(r["label"] for r in rows)),
    }

    if split == "test":
        test_log.parent.mkdir(parents=True, exist_ok=True)
        with test_log.open("a", encoding="utf-8") as fh:
            fh.write(f"{datetime.now().isoformat(timespec='seconds')}\t{config_name}\t"
                     f"{len(answerable)} answerable, {len(unanswer)} unanswerable\n")

    return {"summary": summary, "rows": rows}


def save_run(result: dict, runs_dir: Path = RUNS_DIR) -> Path:
    s = result["summary"]
    path = runs_dir / f"{s['config']}_{s['split']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return path
