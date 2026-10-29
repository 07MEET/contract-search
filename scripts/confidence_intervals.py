"""95% bootstrap confidence intervals for the primary metric (recall@2000 chars) of saved runs.

Usage: python scripts/confidence_intervals.py
"""

import json
import random
from pathlib import Path

RUNS = Path(__file__).resolve().parent.parent / "runs"


def per_query(name):
    rows = json.loads((RUNS / f"{name}.json").read_text(encoding="utf-8"))["rows"]
    return [r["budget_recall"]["2000"] for r in rows if r["answerable"]]


def ci(values, resamples=2000, seed=0):
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(resamples))
    return means[int(0.025 * resamples)], means[int(0.975 * resamples)]


if __name__ == "__main__":
    for name in ("baseline_train", "final_train", "baseline_test", "final_test"):
        values = per_query(name)
        lo, hi = ci(values)
        print(f"{name}: mean {sum(values) / len(values):.3f}  95% CI [{lo:.3f}, {hi:.3f}]  n={len(values)}")
