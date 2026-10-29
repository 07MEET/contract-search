"""Search the contracts from the command line.

    python -m clausesearch.cli "What is the governing law for this contract?" --top 3
"""

import argparse
import json
import re

from clausesearch.retrieve import load_pipeline


def main(argv=None):
    parser = argparse.ArgumentParser(description="Find the clauses that answer a question.")
    parser.add_argument("question")
    parser.add_argument("--config", default="configs/baseline.yaml")
    parser.add_argument("--top", type=int, default=5, help="passages to show")
    parser.add_argument("--json", action="store_true", help="print machine-readable output")
    args = parser.parse_args(argv)

    pipeline = load_pipeline(args.config)
    result = pipeline(args.question)
    passages = [] if result["abstain"] else result["passages"][: args.top]

    if args.json:
        out = [{**p, "text": pipeline.text(p)} for p in passages]
        print(json.dumps({"abstain": result["abstain"], "passages": out}, indent=2))
        return
    if result["abstain"]:
        print("No relevant clause found in the indexed contracts.")
        return
    for rank, p in enumerate(passages, 1):
        start, end = p["span"]
        print(f"\n#{rank}  {p['file_path']}  [{start}:{end}]  score {p['score']:.2f}")
        if p.get("section"):
            print(f"    section: {p['section']}")
        print(re.sub(r"\s+", " ", pipeline.text(p)).strip())


if __name__ == "__main__":
    main()
