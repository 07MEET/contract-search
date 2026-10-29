# Contract Clause Search

## Overview

A clause search system over commercial contracts. Ask a natural-language question about a contract, and it returns a ranked list of the passages most likely to answer it, each with its source file and character offsets. When no passage is relevant enough, it returns nothing and says so.

It runs over the 29 CUAD contracts used by the LegalBench-RAG-mini benchmark and has a web app (Streamlit) and a CLI. Every pipeline choice lives in a YAML config, and a rule-based self-improvement loop changes those configs and keeps a change only when the evaluation on the train split says it helps.

Results and analysis are in [REPORT.md](REPORT.md).

## Setup

**Requirements:** Python 3.14 (tested with 3.14.2 on Windows 11), about 30 MB of disk for the data, and internet access for the one-time download. No GPU, LLM or API keys are needed.

```bash
git clone https://github.com/07MEET/contract-search.git
cd contract-search
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

Install the dependencies (pinned) and download the data:

```bash
pip install -r requirements.txt
python scripts/download_data.py
```

The download fetches only `benchmarks/cuad.json` and `corpus/cuad/` from the [LegalBench-RAG mirror](https://huggingface.co/datasets/awinml/legalbench-rag), pinned to one dataset revision, into `data/` (gitignored). All other commands run from the repository root with the venv active.

## How to run

| Task | Command |
|---|---|
| Web app | `streamlit run app.py`, then open http://localhost:8501 and pick a config (`final` or `baseline`) in the sidebar |
| CLI | `python -m clausesearch.cli "Consider the Cooperation Agreement between HPIL ENERGYTECH Inc. and GINARES GROUP AG for Renewable Energy Projects; What is the governing law for this contract?" --config configs/final.yaml --top 3` |
| CLI, JSON output | add `--json` |
| Evaluate a config | `python -m clausesearch.evaluate --config configs/final.yaml --split train` (or `--split test`) |
| Error report for a run | `python scripts/error_report.py runs/final_train.json` (writes `runs/final_train_errors.md`) |
| Confidence intervals | `python scripts/confidence_intervals.py` |
| Improvement loop | `python -m clausesearch.loop` |
| Tests | `python -m pytest -q` |

Questions should name their contract in the benchmark's form, `Consider the <contract>; <question>`, because the final pipeline uses that part to pick the contract (see Assumptions).

## Architecture

```
scripts/download_data.py ─► data/ (cuad.json + 462 contracts)
                                │
clausesearch/data.py ───────────┘  194 mini queries + train/test split + the 29 referenced contracts, offsets verified
        │
clausesearch/retrieve.py   Pipeline(config, corpus): chunking, BM25 index, contract routing, stemming,
        │                  stopwords, section headings, abstention  ─►  pipeline(query) -> passages + abstain
        ├──► clausesearch/cli.py, app.py                    the two interfaces
        ├──► clausesearch/evaluate.py                       character-level P@k / R@k, budget recall, abstention,
        │                                                   failure labels  ─►  runs/<config>_<split>.json
        └──► clausesearch/loop.py                           evaluate on train ─► diagnose ─► rule proposes a config change
                                                            ─► accept/reject by experiments/objective.yaml
                                                            ─► experiments/log.jsonl, configs/final.yaml
```

| Path | What lives there |
|---|---|
| `configs/baseline.yaml`, `configs/final.yaml` | Pipeline configurations. `final.yaml` is written by the loop. Every option is documented in `clausesearch/retrieve.py`, and options a config omits take their baseline value |
| `experiments/objective.yaml` | The loop's primary metric, acceptance rule and guardrails |
| `experiments/log.jsonl` | Every loop iteration from every run, accepted or rejected |
| `experiments/configs/` | The candidate config of every iteration |
| `experiments/test_runs.log` | One line per test-split evaluation, written automatically |
| `eval/unanswerable.jsonl` | 45 labelled unanswerable queries (frozen in commit `b7ca2c5`), built by `scripts/build_unanswerable.py` |
| `runs/` | Saved evaluation runs (summary plus one row per query) and their error reports |
| `tests/` | Tests for data loading, metrics, retrieval, headings, the loop's decision logic, the unanswerable set and the app |

## Reproducing results

From a fresh clone, after Setup (dependency install about 2–3 min, data download about 3 min):

| Step | Command | Time | Reproduces |
|---|---|---|---|
| 1 | `python -m pytest -q` | ~2 s | all tests pass |
| 2 | `python -m clausesearch.evaluate --config configs/baseline.yaml --split train` | ~5 s | baseline train numbers in REPORT §5 |
| 3 | `python -m clausesearch.evaluate --config configs/final.yaml --split train` | ~5 s | final train numbers |
| 4 | `python -m clausesearch.evaluate --config configs/baseline.yaml --split test` | ~5 s | baseline test numbers |
| 5 | `python -m clausesearch.evaluate --config configs/final.yaml --split test` | ~5 s | final test numbers |
| 6 | `python scripts/confidence_intervals.py` | ~2 s | the 95% intervals in REPORT §5 (needs steps 2–5) |
| 7 | `python -m clausesearch.loop` | ~30 s | the iteration history in REPORT §6: it replays run 4 from the baseline and ends at the same `configs/final.yaml` |

Everything is deterministic (BM25, a seeded bootstrap, no model calls), so the numbers match exactly. Note that steps 2–7 overwrite the files in `runs/`, steps 4–5 append lines to `experiments/test_runs.log`, and step 7 appends a new run to `experiments/log.jsonl`. The test-run count in the report refers to the two lines committed in `e814a14`.

## Assumptions

Where the brief was unclear, these are the decisions taken and why.

1. **Private repository.** The brief asks for a private repository in one place and a public one in another. I followed the submission instruction (private, with collaborator access), which also suits the brief's confidentiality terms.
2. **Overlapping retrieved spans are merged before scoring.** The authors' scoring code adds up retrieved spans as they are, so overlapping chunks would count the same characters twice. Merging per file avoids that; with non-overlapping chunks the two definitions give identical numbers.
3. **How abstentions count in precision and recall.** An abstention on an answerable query scores 0 in the end-to-end numbers. Retrieval-only numbers (the ranked list, ignoring abstention) are reported separately, so search quality and abstention quality can be judged apart. Unanswerable queries have no gold text, so they count only toward the abstention metrics.
4. **k counts passages.** P@k and R@k use k = number of passages, as in the paper, for comparability. Because they change with chunk size, I also report recall at fixed character budgets (500 / 1,000 / 2,000 / 4,000), and the loop's primary metric is recall at 2,000 characters.
5. **Reading files.** Contracts are read as UTF-8 in Python's default text mode, and file paths are NFC-normalised (one CUAD `file_path` is NFD while its file name is NFC). All 272 gold spans are checked at load time: `doc[start:end] == answer`.
6. **The split.** `mini()` and `assign_split()` are used exactly as given. This gives 140 train / 54 test benchmark queries (28% test) and 29 / 16 unanswerable queries (36% test).
7. **Duplicate queries.** The full CUAD file has duplicates, but the 194 mini queries contain none, so no handling was needed. Duplicates would land in the same split anyway, because the split hashes the query text.
8. **Queries name their contract.** Every benchmark query begins with "Consider the <contract>;". The final pipeline uses this to pick one contract, and declines a query that has no such part. A real tool would need a contract picker instead.
9. **Unanswerable queries.** I took "the indexed contracts don't answer it" to cover a clause missing from an indexed contract, media-style questions those contracts don't address, contracts that are not indexed, and off-topic questions. Absence was checked by keyword search over the contract text plus manual review of every hit, not by a legal expert. The set was committed before any tuning and never edited.
10. **Threshold changes in the loop.** Abstention thresholds don't change the ranked list, so they cannot move the retrieval-only primary metric. I added an acceptance rule for them (correct abstention +0.05, guardrails hold) to the objective before the loop's first run (commit `418be06`).
11. **Test runs.** Test was evaluated twice in total, once for the baseline and once for the final config, both after all tuning (`experiments/test_runs.log`). The brief asks for baseline vs final on test, so I counted both.
12. **Python 3.14.** The newest stable Python available. Python 3.10, the other version installed, reached end of life in October 2026.

## AI tool usage

- **Claude Code (Anthropic), in the Claude desktop app**, was used throughout as a pair programmer. It read the brief, the dataset card, the LegalBench-RAG paper and the authors' scoring code, and summarised them. It proposed the plan and wrote most of the code, the tests, `REPORT.md` and this README. It also ran the commands, checked intermediate results (offset checks, sanity runs with known scores), and found and fixed bugs in the loop, which are recorded in the log and the report.
- **My role:** I directed each step and approved the plan and objective. I reviewed and approved the unanswerable set before freezing it, chose the STAIR-inspired stretch goal, tested the CLI and web app by hand with known-answer queries, and reviewed the report. I can explain and modify every part of the code.
- **No LLM is used inside the system** (see REPORT §3).
