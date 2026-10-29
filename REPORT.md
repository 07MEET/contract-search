# Evaluation Report: Contract Clause Search

## 1. Summary

I built a clause search system over the 29 CUAD contracts referenced by the 194 LegalBench-RAG-mini CUAD queries. For a question, it returns ranked passages with file and character offsets, or says that no relevant clause exists. It has a CLI and a Streamlit app. The final pipeline is plain BM25 with four changes, each chosen by a rule-based self-improvement loop on train only:
- route each query to one contract using its "Consider the …" description, and rank passages with the question alone;
- stem words;
- drop question-template words;
- use 500-character chunks that overlap by half;

plus two abstention thresholds found by grid search.

**On the held-out test split (54 answerable, 16 unanswerable queries), recall at a 2,000-character reading budget rose from 0.064 to 0.515** (95% CI 0.400–0.631; train 0.527). R@1 is 0.323, R@64 is 0.840, and P@1 is 0.254. The system correctly declines 50% of unanswerable test queries (4/4 about unindexed contracts, 4/10 about missing clauses, 0/2 media questions), and wrongly declines 5.6% of answerable ones. Test was evaluated exactly twice, once for the baseline and once for the final config, after all tuning had finished. No LLM is used.

## 2. System design

```
query ──► split at ";" ──► contract description ──► BM25 over contract headers (file name + first 2,000 chars) ──► best contract
                         └► question ──► tokenize (lowercase, drop template words, Snowball stem)
                                         └► BM25 over that contract's 500-char chunks (250 overlap) ──► top 64 passages
abstain if contract-match score < 22.16  or  best passage score <= 2.95
```

Every option is a key in a YAML config ([configs/baseline.yaml](configs/baseline.yaml), [configs/final.yaml](configs/final.yaml)). Nothing that affects results is hard-coded.

| Decision | Chosen | Alternatives considered, and why not |
|---|---|---|
| Retriever | BM25 (`rank-bm25`) | **Dense embeddings / hybrid.** Not tried in the time available. They are the most likely next gain (see §8), but would need a model download and a privacy review. **LLM reranking.** See §3 |
| Search scope | **Route to one contract, then search within it** | Searching all 29 contracts with the full query (baseline): the contract name in the query pulled each contract's **title page and signature block** to rank 1 (R@1 = 0.000). Routing raised the primary from 0.030 to 0.301 |
| Tokens | Snowball stemming, drop 34 template words | Raw words miss "expiration" vs "expire". Stemming gave +0.129 on the primary |
| Chunking | 500 chars, 250 overlap | 250 chars (rejected, bootstrap win 0.896 < 0.90); 1,000 chars (rejected, −0.025); no overlap (baseline) |
| Structure | **Not used** (tested and rejected) | A **STAIR-inspired** section-heading index. STAIR ([arXiv 2609.03874](https://arxiv.org/abs/2609.03874)) fine-tunes a 7B LLM to generate the table-of-contents leaf that answers a query. As designed it needs an existing table of contents, about 62k training queries and GPU fine-tuning, and it returns section titles rather than spans. None of that fits 29 plain-text contracts, 140 train queries and character-level scoring. I tested its core idea instead: [`find_headings`](clausesearch/retrieve.py) builds a heading path for each contract with a regex (24/29 contracts get ≥ 3 headings; 131/140 train gold spans fall in a detected section), and each chunk is indexed with its section path. **Rejected** (primary 0.527 → 0.511); see §6 and §7 |
| Abstention | Two thresholds: contract match and passage score | A single passage-score threshold: it cannot tell "contract not indexed" from "clause missing" |
| Metric code | Own implementation of the authors' definition, with span merging | The authors' code does not merge overlapping retrieved spans, which can double-count characters. Ours merges them per file; with non-overlapping chunks the two give identical results |

## 3. LLM use

**None.**
- **No measured need.** The largest remaining errors come from vocabulary gaps, which embeddings address more cheaply than an LLM.
- **Reproducibility.** BM25 is deterministic, and a full loop run takes 30 s on a laptop.
- **Privacy.** The deciding factor for a real deployment. JioStar's contracts are confidential, so a hosted LLM would send clause text to a third party. A local model (e.g. via Ollama) avoids that, but adds latency and hardware cost that would need to be justified by a measured gain I did not have time to measure.

The most promising LLM use would be reranking the top 20 passages, with all outputs cached so evaluation stays reproducible.

## 4. Evaluation setup

| Item | Detail |
|---|---|
| Queries | 194 LegalBench-RAG-mini CUAD queries, selected with the authors' `mini()` function; **140 train / 54 test** via the fixed `assign_split` |
| Corpus | The 29 contracts those queries refer to (1.21M characters). All 272 gold spans verified: `doc[start:end] == answer` |
| Unanswerable set | 45 queries in [eval/unanswerable.jsonl](eval/unanswerable.jsonl): **29 train / 16 test**; 26 clause missing from an indexed contract, 6 media questions, 8 contracts not indexed, 5 off-topic. Built by keyword search over the contract text with every hit reviewed ([scripts/build_unanswerable.py](scripts/build_unanswerable.py)), committed in `b7ca2c5` before any tuning, and never edited |
| Retrieval metrics | Character-level precision and recall at k ∈ {1, 2, 4, 8, 16, 32, 64} (k = passages), averaged over answerable queries. **Recall at character budgets** of 500, 1,000, 2,000 and 4,000 (passages taken in rank order, the last one cut), because P@k and R@k change with chunk size. Reported **retrieval-only** (the ranked list, ignoring abstention) and **end-to-end** (an abstention on an answerable query scores 0) |
| Abstention metrics | False abstention rate on answerable queries; correct abstention rate on unanswerable queries |
| Failure labels | Per answerable query at k = 8: `wrong_document`, `wrong_section`, `partial_span` (< 50% of gold covered), `hit`, `false_abstain`. Per unanswerable query: `correct_abstain` or `false_answer` |
| Use of the split | All development, rules and thresholds used **train only**. The loop drops test queries before it runs. Test was run **2 times** in total, once per config, as logged in [experiments/test_runs.log](experiments/test_runs.log) |

Note: the budget counts every character shown, so overlapping chunks use up budget twice. This works against the overlap setting, so its measured gain is conservative.

## 5. Results

Primary metric in bold. n = answerable / unanswerable queries behind each column.

| Metric | Baseline train (140/29) | Baseline test (54/16) | Final train (140/29) | **Final test (54/16)** |
|---|---|---|---|---|
| **Recall @2,000 chars** | 0.030 | 0.064 | 0.527 | **0.515** |
| 95% bootstrap CI | 0.009–0.056 | 0.011–0.130 | 0.445–0.608 | 0.400–0.631 |
| Recall @500 / @1,000 / @4,000 | 0.000 / 0.008 / 0.092 | 0.000 / 0.015 / 0.129 | 0.336 / 0.417 / 0.584 | 0.323 / 0.428 / 0.632 |
| R@1 / R@8 / R@64 | 0.000 / 0.089 / 0.366 | 0.000 / 0.123 / 0.364 | 0.332 / 0.584 / 0.873 | 0.323 / 0.632 / 0.840 |
| P@1 / P@8 | 0.000 / 0.011 | 0.000 / 0.015 | 0.246 / 0.091 | 0.254 / 0.107 |
| R@8 end-to-end | 0.089 | 0.123 | 0.542 | 0.632 |
| False abstention | 0.000 | 0.000 | 0.079 (11/140) | 0.056 (3/54) |
| Correct abstention | 0.000 | 0.000 | 0.586 (17/29) | 0.500 (8/16) |
| Seconds per query | 0.006 | 0.006 | 0.002 | 0.003 |

Correct abstention by category, final config:

| Category | Train | Test |
|---|---|---|
| Contract not indexed | 4/4 | 4/4 |
| Off-topic | 5/5 | none in test |
| Clause missing from an indexed contract | 8/16 | 4/10 |
| Media question | 0/4 | 0/2 |

**Train–test gap.** The primary metric differs by 0.012 (0.527 vs 0.515), well inside both confidence intervals. The accepted changes are general (routing, stemming, stopwords, overlap) rather than tuned to individual queries, which is consistent with the small gap. The two thresholds are the most train-specific parameters. On test, false abstention was lower (0.056) and correct abstention lower (0.500 vs 0.586), and with 16 unanswerable test queries each one is 6 points.

**Context.** The paper reports CUAD R@64 of 0.757 with OpenAI embeddings and naive chunking over the whole mini corpus, against 0.840 here. That is not a like-for-like comparison: we index only the CUAD contracts, and we use the contract name for routing.

## 6. Iteration history

**Objective**, declared in [experiments/objective.yaml](experiments/objective.yaml) and committed before the loop existed:
- **Primary metric:** recall @2,000 chars on train, retrieval-only. Missing a clause is worse than reading extra text, and the budget stops bigger chunks from looking better just by returning more text.
- **Acceptance:** a gain of ≥ 0.01 that wins ≥ 90% of 1,000 paired bootstrap resamples.
- **Guardrails:** false abstention ≤ 0.10; correct abstention may not drop more than 0.05; recall @500 may not drop more than 0.02; ≤ 1 s per query.
- **Amendment** (committed before the loop's first run): threshold-only changes cannot move the retrieval-only primary, so they are judged on correct abstention (+0.05) instead.

**How the loop works.** `python -m clausesearch.loop` ([clausesearch/loop.py](clausesearch/loop.py)) starts from the baseline and repeats:
1. Evaluate on train.
2. Count the failure labels.
3. Take the first rule (in a fixed order) whose trigger fires on that diagnosis.
4. Evaluate the changed config.
5. Accept or reject it by the objective.
6. Append the iteration to [experiments/log.jsonl](experiments/log.jsonl) with its change, reason, proposer, metrics before and after, win rate and decision.

Proposals come from 7 hand-written rules plus one parameter search (the abstention grid). A rule's trigger is, for example, "≥ 30% of queries reach the right contract but the wrong section". Every candidate config is saved in [experiments/configs/](experiments/configs/).

**Final run (run 4).** Primary = recall @2,000 chars on train.

| Iter | Proposer | Change | Why it was tried | Primary | R@64 | Correct abst. | Win | Decision |
|---|---|---|---|---|---|---|---|---|
| 0 | human | baseline | simplest pipeline | 0.030 | 0.366 | 0.000 | — | baseline |
| 1 | rule: route_by_title | route by contract name | 81% wrong section; title and signature chunks rank first | **0.301** | 0.845 | 0.000 | 1.00 | accepted |
| 2 | rule: stem | Snowball stemming | many answers below rank 8; "expiration" vs "expire" | **0.430** | 0.904 | 0.000 | 1.00 | accepted |
| 3 | rule: smaller_chunks | 250-char chunks | median train gold span 314 chars | 0.460 | 0.779 | 0.000 | 0.896 | **rejected** (win < 0.90) |
| 4 | rule: overlap | 250-char overlap | partial spans: clauses cut at chunk edges | **0.465** | 0.872 | 0.000 | 0.934 | accepted |
| 5 | rule: stopwords | drop template words | "is there", "this", "under" add noise | **0.527** | 0.873 | 0.138 | 1.00 | accepted |
| 6 | rule: section_headings | STAIR-inspired heading index | 34% still wrong section | 0.511 | 0.878 | 0.138 | 0.06 | **rejected** (−0.016) |
| 7 | parameter search | abstention thresholds | 25/29 unanswerable still answered | 0.527 | 0.873 | **0.586** | — | accepted (false abst. 0.079) |

**Earlier runs**, kept in the log, each exposed a bug in the loop and so are part of the record:

| Run | What happened | Fix |
|---|---|---|
| 1 | The stemming rule never fired. Its trigger, "answer missing from the top 64", became rare once routing limited the search to one contract. Smaller chunks, overlap and stopwords were all rejected *without* stemming | Trigger changed to "answer below rank 8" |
| 2 | Calibration was rejected at false abstention 0.157, although the search had kept it ≤ 0.10. Every query about one contract shares one contract-match score, and rounding the threshold to 4 decimals pushed it above 11 such queries | Thresholds placed at midpoints between observed scores, unrounded |
| 3 | The same as run 4 without the section-heading rule | — |

Rejected ideas in total: smaller chunks (×4), larger chunks, overlap and stopwords without stemming (run 1), section headings, and one buggy calibration.

## 7. Error analysis

13 failures from the final config, grouped by cause. Offsets refer to the contract file named. Full listings: [runs/final_test_errors.md](runs/final_test_errors.md), [runs/final_train_errors.md](runs/final_train_errors.md).

**A. The clause does not use the question's words (vocabulary gap).** This is the largest group, and keyword search cannot solve it.

| # | Split | Query (contract; question) | Gold clause | What happened |
|---|---|---|---|---|
| 1 | test | Dynamex transport services; exclusivity? | 7970–8101 "Dynamex agrees not to provide sameday delivery services for any other provider…" | Not in the top 64. The clause never says "exclusive" |
| 2 | test | ISA–Rubicon alliance; covenant not to sue? | 13844–13911 "Rubicon shall not contest ownership by ISA…" (+2 spans) | Not in the top 64. "Contest" is never linked to "sue" |
| 3 | train | Theravance service agreement; termination for convenience? | 18678–18997 "The Company may, in its sole and absolute discretion, terminate…" | Rank 17. No "convenience" in the clause |
| 4 | test | BicycleTX service agreement; expiration date? | 693–859 "Your employment shall commence on 26 September 2019 and shall continue unless and until…" | Rank 16, and the query was declined anyway (#11). Open-ended terms never say "expire" |
| 5 | test | Union Dental affiliate agreement; audit rights? | 3636–4076 "Make available … all records, books, agreements…" | Rank 20. The audit right is described, never named |

*Diagnosis:* BM25 matches words, not meaning. *Fix:* dense or hybrid retrieval, or a small legal synonym map per clause type (exclusive ↔ "not … for any other"; sue ↔ contest/challenge).

**B. Boilerplate matches the question better than the clause does (lexical trap).**

| # | Split | Query | What happened |
|---|---|---|---|
| 6 | test | Dynamex; termination for convenience? | Rank 1 is "26.0 HEADINGS AND CAPTIONS … for convenience only", the only place "convenience" appears. Gold (33227–33332, "Either Party may terminate … without cause") is at rank 10 |
| 7 | test | Igene joint venture; audit rights? | Gold (62830–62977) says "auditors review the books". Snowball stems "auditors" to `auditor` but "audit" to `audit`, so they never match. Rank 22 in a 70k-char contract |

*Diagnosis:* a single rare word dominates the BM25 score. *Fix:* a reranker that reads the whole passage, or lemmatisation instead of stemming.

**C. Answers that are long or split into several pieces (partial span).**

| # | Split | Query | What happened |
|---|---|---|---|
| 8 | test | King/Depomed promotion; right of first refusal/offer/negotiation? | Rank 1 is the right section ("Section 13.2 Right of First Negotiation"), but the three gold spans total about 3,400 chars, more than the 2,000-char budget. Recall @8 is 0.42 |
| 9 | test | Papa John's endorsement; non-disparagement? | Two gold spans 48k chars apart (13350 and 61086). It finds the area of the second ("10. Confidentiality and Non-Disparagement", rank 1) but not the first. Recall @8 is 0.33 |

*Diagnosis:* each passage is ranked independently, so a second relevant location must compete with neighbours of the first. *Fix:* merge adjacent passages, and add diversity across sections to the ranking.

**D. Abstention errors.**

| # | Split | Query | What happened |
|---|---|---|---|
| 10 | test | ALCO/GE Capital agency; cap on liability? (unanswerable) | Answered. After preprocessing the question is `cap liabil contract`, and "contract" (found in 23 of 29 contracts) matched "lease contract" with score 4.31, above the 2.95 threshold |
| 11 | train + test | BicycleTX; 5 different questions | All declined. The contract-match score of the BicycleTX description is 21.14, under the 22.16 threshold, so **every** question about this contract is refused. A threshold tuned on raw BM25 scores works per contract, not per question |
| 12 | train | Glu Mobile license amendment; sublicense to a streaming service? (unanswerable) | Answered with the amendment's title paragraph ("…Wireless Content License Agreement…", score 8.66), which shares "content" and "license" with the question. The amendment says nothing about sublicensing. 0/6 media questions were declined |

*Diagnosis:* raw BM25 scores are not calibrated probabilities. They depend on query length and on the contract, so one threshold cannot separate "clause missing" from "clause present". *Fix:* normalise scores (per query, or by the score of a contract-wide "no clause" baseline), or train a small classifier on the score distribution.

**E. Label ambiguity.**

| # | Split | Query | What happened |
|---|---|---|---|
| 13 | test | ISA–Rubicon; services after termination? | Gold (12612–12792) is "Each Party shall retain the financial records … for six years", a record-keeping duty rather than a service. The system returned the contract-services clauses. Some CUAD categories are broad, so a few "failures" are defensible answers |

## 8. Limitations and next steps

**What doesn't work yet**
- **Absent clauses.** The system declines only 12 of the 26 missing-clause queries across train and test, and none of the 6 media questions. A legal user cannot yet trust "the system returned something" as evidence that the clause exists.
- **Contract-level abstention.** Because the contract-match threshold works per contract, one weakly described contract (BicycleTX) is refused entirely.
- **Synonyms and paraphrase.** Group A shows exclusivity, covenant-not-to-sue and audit clauses that don't use the query's words.
- **Assumes the query names its contract.** Every benchmark query does. With routing on, a query with no "Consider the …;" part has a contract-match score of 0, so it is always declined, and its ranked list comes from one arbitrary contract. A real tool needs a contract picker, or a fallback that searches all contracts.
- **Small evaluation.** 54 test answerable queries give a 95% CI about ±0.115 wide. Test has only 16 unanswerable queries and no off-topic ones.
- **Unanswerable set quality.** It is verified by keyword search and manual review, not by legal experts. An unusually worded clause could have been missed.
- **Cross-references and definitions** ("as defined in Section 4.2") are not resolved.

**What would need to change before legal users relied on it**
1. Hybrid BM25 + dense retrieval with a cross-encoder reranker, run **locally** for confidentiality, measured by this same loop.
2. Calibrated abstention: normalised scores, or a classifier, with a reported precision for "no clause found" claims.
3. Always show the section heading and surrounding text (the app already does), so users can check context quickly.
4. Resolve definitions and cross-references at indexing time. The heading parser from the STAIR experiment is a starting point, used as a filter followed by span ranking within a section rather than as a score boost.
5. A larger, expert-labelled evaluation, including real JioStar question types, contracts without a name in the query, and multi-contract questions.
6. With more labelled data, a STAIR-style section router trained on contract tables of contents.
