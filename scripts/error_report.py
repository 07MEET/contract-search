"""Turn a saved run into a readable error report grouped by failure label.

Usage: python scripts/error_report.py runs/baseline_train.json [--per-label 4]
Writes runs/<config>_<split>_errors.md next to the run file.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from clausesearch.data import load  # noqa: E402

LABEL_ORDER = ["wrong_document", "wrong_section", "partial_span", "false_abstain", "false_answer", "hit", "correct_abstain"]


def excerpt(corpus, item, limit=300):
    start, end = item["span"]
    text = re.sub(r"\s+", " ", corpus[item["file_path"]][start:end]).strip()
    return text[:limit] + ("..." if len(text) > limit else "")


def passage_line(corpus, rank, p):
    name = p["file_path"].split("/", 1)[1][:60]
    return f"{rank}. `{name}` [{p['span'][0]}:{p['span'][1]}] score {p['score']:.2f}: {excerpt(corpus, p)}"


def report(run, corpus, per_label):
    s = run["summary"]
    groups = defaultdict(list)
    for row in run["rows"]:
        groups[row["label"]].append(row)

    lines = [
        f"# Error report: {s['config']} on {s['split']}",
        "",
        f"{s['n_answerable']} answerable and {s['n_unanswerable']} unanswerable queries. "
        f"Labels use the top {s['label_k']} passages.",
        "",
        "| Label | Count |",
        "|---|---|",
        *(f"| {label} | {len(groups[label])} |" for label in LABEL_ORDER if groups[label]),
    ]
    for label in LABEL_ORDER:
        rows = groups[label]
        if not rows or label in ("hit", "correct_abstain"):
            continue
        lines += ["", f"## {label} ({len(rows)})"]
        for row in rows[:per_label]:
            lines += ["", f"**Query:** {row['query']}", ""]
            if row["answerable"]:
                rank = row["first_hit_rank"]
                lines.append(f"First relevant passage at rank: {rank if rank else 'not in top 64'}; "
                             f"recall@{s['label_k']}: {row['recall'][str(s['label_k'])]:.2f}")
                lines += ["", "Gold:"]
                lines += [f"- `{g['file_path'].split('/', 1)[1][:60]}` [{g['span'][0]}:{g['span'][1]}]: {excerpt(corpus, g)}"
                          for g in row["gold"]]
            else:
                lines.append(f"Unanswerable ({row['category']}), but the system answered.")
            lines += ["", "Returned:"]
            lines += [passage_line(corpus, i, p) for i, p in enumerate(row["top_passages"][:3], 1)]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run")
    parser.add_argument("--per-label", type=int, default=4)
    args = parser.parse_args()

    run_path = Path(args.run)
    run = json.loads(run_path.read_text(encoding="utf-8"))
    _, corpus = load()
    out = run_path.with_name(run_path.stem + "_errors.md")
    out.write_text(report(run, corpus, args.per_label), encoding="utf-8")
    print(f"wrote {out}")
