"""Build eval/unanswerable.jsonl. Re-runs every keyword check and records the hit counts."""
import json, re, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from clausesearch.data import DATA_DIR, assign_split, load, nfc

queries, corpus = load()
prefix = {}
for q in queries:
    prefix[q["snippets"][0]["file_path"]] = q["query"].split(";", 1)[0].strip()
full = json.loads((DATA_DIR / "benchmarks/cuad.json").read_text(encoding="utf-8"))["tests"]
benchmark_queries = {t["query"].strip() for t in full}


def fp(short):
    return next(f for f in corpus if f.split("/")[1].startswith(short))


GOV = r"govern|laws of|jurisdiction|construed|venue"
ASG = r"assign|transfer|successor"
CAP = r"liabilit|liable|in no event|shall not exceed|limit(ed|ation)? (to|of)|consequential"
AUD = r"audit|inspect|books|records|examin"
INS = r"insur|insured|coverage"
EXC = r"exclusiv|sole "
COC = r"change (of|in) control|merger|acqui|controlling|reorgani"
CMP = r"compet|non-compet|restrict"
REN = r"renew|extend|extension|evergreen|successive"
REV = r"royalt|profit|revenue|percent|%|commission"

T_GOV = "What is the governing law for this contract?"
T_ASG = "Is there an anti-assignment clause in this contract?"
T_CAP = "Is there a cap on liability under this contract?"
T_AUD = "What are the audit rights under this contract?"
T_INS = "What are the insurance requirements under this contract?"
T_EXC = "Does this contract include an exclusivity agreement?"
T_COC = "What happens in the event of a change of control of one of the parties in this contract?"
T_CMP = "Is there a non-compete clause in this contract?"
T_REN = "What is the renewal term for this contract?"
T_REV = "Does this contract include any revenue or profit-sharing arrangements?"
T_IP = "How is intellectual property ownership assigned in this contract?"
T_EXP = "What is the expiration date of this contract?"

# (contract prefix, question, keyword pattern, reviewer note on any hits)
MISSING = [
    ("ALCOSTORES", T_GOV, GOV, ""),
    ("ArcGroupInc", T_GOV, GOV, "only hit: 'construed' in an invoicing sentence"),
    ("GluMobileInc", T_GOV, GOV, ""),
    ("RgcResources", T_GOV, GOV, "only hit: 'Avenue' in a notice address"),
    ("UnionDental", T_ASG, ASG, ""),
    ("ArcGroupInc", T_ASG, ASG, ""),
    ("ALCOSTORES", T_CAP, CAP, ""),
    ("HOLIDAYRV", T_CAP, CAP, ""),
    ("WESTERN COPPER", T_CAP, CAP, "hits are 'limited liability company' and 'not limited to' only"),
    ("BICYCLETHERA", T_CAP, CAP, "hits are 'not limited to' only"),
    ("CANOPETROLEUM", T_AUD, AUD, ""),
    ("HPILHOLDING", T_AUD, AUD, ""),
    ("Loop Industries", T_AUD, AUD, ""),
    ("PapaJohns", T_AUD, AUD, ""),
    ("PcquoteCom", T_INS, INS, ""),
    ("HealthcareIntegrated", T_INS, INS, ""),
    ("VITAMINSHOPPE", T_INS, INS, ""),
    ("DUOSTECHNOLOGIES", T_INS, INS, ""),
    ("FLOTEK", T_EXC, EXC, "only hit: 'sole responsibility' for safety precautions"),
    ("THERAVANCE", T_COC, COC, ""),
    ("PenntexMidstream", T_CMP, CMP, "only hit: 'Restrictions on Assignment' heading"),
    ("BONTONSTORES", T_CMP, CMP, "hits are legal/lease 'restrictions' in sale guidelines, no non-compete"),
    ("UnionDental", T_CMP, CMP, "only hit: confidentiality 'restrictions'"),
    ("DeltathreeInc", T_REN, REN, ""),
    ("MJBIOTECH", T_REN, REN, ""),
    ("ON2TECHNOLOGIES", T_REV, REV, "only hit: 'Securities and Exchange Commission'"),
]

MEDIA = [
    ("GluMobileInc", "Can the licensee pass these content rights on to another streaming service by sublicense?",
     r"sublicens|sub-licens|third part|platform", ""),
    ("VEONEER", "Until what date does any exclusive arrangement between the parties last?", EXC, ""),
    ("HOLIDAYRV", "Which party owns the intellectual property in works derived from the licensed marks?",
     r"derivative|owner|own(s|ed)? |property of|title to", ""),
    ("PcquoteCom", "Which party owns the intellectual property in derivative works created from the co-branded content?",
     r"derivative|owner|title to|property of", ""),
    ("CANOPETROLEUM", "May the episodes of the show be streamed online or distributed outside the United States?",
     r"stream|internet|online|digital|territor|region|international", ""),
    ("VITAMINSHOPPE", "Does this contract permit the sponsored content to be dubbed or translated into other languages?",
     r"dub|translat|language|subtitl", ""),
]

NOT_IN_CORPUS = [
    "Consider the Co-Branding and Advertising Agreement between i-Escrow, Inc. and 2TheMart.com, Inc.; " + T_GOV,
    "Consider the Endorsement Agreement between Tom Watson and Adams Golf, Ltd.; " + T_AUD,
    "Consider the Multiple LINAC and Multi-Modality Distributor Agreement of Accuray Incorporated; " + T_ASG,
    "Consider the Services Agreement between a confidential provider and Telcostar Pte, Ltd.; " + T_CAP,
    "Consider the Content Licensing Agreement between Starlight Pictures Pvt. Ltd. and Meridian Streaming Inc. for a regional film library; " + T_GOV,
    "Consider the Co-Production Agreement between Blue Lotus Studios and Harbor Bay Media for the series 'Monsoon Diaries'; " + T_IP,
    "Consider the Distribution Agreement between Northwind Broadcasting and Tamarind Digital for cricket highlights; " + T_ASG,
    "Consider the Music Synchronization License between Raga Records and Kestrel Lane Productions; " + T_EXP,
]

OFF_TOPIC = [
    "What is the statutory limitation period for breach of contract claims in India?",
    "How do I register a trademark for the title of a new show?",
    "Which of our agreements were signed in 2023?",
    "What GST rate applies to OTT subscription fees?",
    "What is the difference between a licence and an assignment of copyright?",
]

records = []


def add(query, category, contract, note):
    assert query.strip() not in benchmark_queries, f"collides with a benchmark query: {query}"
    records.append({"id": f"U{len(records) + 1:02d}", "query": query, "category": category,
                    "contract": contract, "split": assign_split(query), "verification": note})


for group, category in ((MISSING, "missing_clause"), (MEDIA, "media_question")):
    for short, question, pat, review in group:
        f = fp(short)
        n = len(re.findall(pat, corpus[f], re.I))
        note = f"searched /{pat}/ (case-insensitive): {n} hits" + (f"; {review}" if review else "")
        assert n == 0 or review, f"unreviewed hits for {short}: {question}"
        add(f"{prefix[f]}; {question}", category, f, note)

for q in NOT_IN_CORPUS:
    add(q, "contract_not_indexed", None, "contract is not among the 29 indexed contracts")
for q in OFF_TOPIC:
    add(q, "off_topic", None, "general question no single contract clause answers")

out = REPO / "eval" / "unanswerable.jsonl"
out.parent.mkdir(exist_ok=True)
with out.open("w", encoding="utf-8", newline="\n") as fh:
    for r in records:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"wrote {len(records)} queries to {out}")
print("by category:", dict(Counter(r["category"] for r in records)))
print("by split:", dict(Counter(r["split"] for r in records)))
for r in records:
    print(f"{r['id']} [{r['split']:5}] {r['category']:20} {r['query']}")
