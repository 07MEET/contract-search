import json
from pathlib import Path

from clausesearch.data import assign_split

PATH = Path(__file__).resolve().parent.parent / "eval" / "unanswerable.jsonl"


def test_unanswerable_set_is_well_formed():
    records = [json.loads(line) for line in PATH.read_text(encoding="utf-8").splitlines()]
    assert len(records) >= 30
    assert len({r["query"] for r in records}) == len(records)
    for r in records:
        assert r["split"] == assign_split(r["query"])
        assert r["category"] in {"missing_clause", "media_question", "contract_not_indexed", "off_topic"}
