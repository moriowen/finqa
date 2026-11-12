# FinanceBench QA with provenance: a comparative study

An experiment on the 150 FinanceBench questions. It compares Qwen3.5 models at three sizes (2B, 9B, 27B), with and without a checking pipeline (the "harness"). For every question, each configuration gives an answer with the PDF page, quote and passage behind it, or it refuses and says why. The goal is to learn which model and which setup to use for a later project. This repository does not build a product.

- **Demo: https://finqa-demo.vercel.app.** It replays recorded runs step by step, lets you browse every configuration's 150 answers with the cited pages, and shows the system diagrams. The same page is in [`viewer/index.html`](viewer/index.html) and opens locally without a server.
- **Write-up:** [`docs/report.pdf`](docs/report.pdf), 2 pages plus the diagram on page 3.
- **All answers with provenance:** [`results/answers.md`](results/answers.md) (9B), [`results/answers-all-27b-full.md`](results/answers-all-27b-full.md), [`results/answers-all-2b-full.md`](results/answers-all-2b-full.md), [`results/answers-pathb-27b-full.md`](results/answers-pathb-27b-full.md).

## Experiments

Three experiments on the same 150 questions, plus a latency benchmark. Every configuration is reported as three counts out of 150: correct, wrong, refused (decision A24 in [`docs/assumptions.md`](docs/assumptions.md)). No configuration is "the official one". The tables are the comparison. 2B was dropped after experiment 1, because it answers too few questions to be useful.

### Experiment 1: the document is given

FinanceBench gives each question with its filing, so the system only has to read that filing and answer. This tests **reading**.

| Model | Setting | Correct | Wrong | Refused |
|---|---|---|---|---|
| Qwen3.5-2B | bare | 77 | 72 | 1 |
| Qwen3.5-2B | full harness | 12 | 2 | 136 |
| Qwen3.5-9B | bare | 93 | 57 | 0 |
| Qwen3.5-9B | full harness | 72 | 16 | 62 |
| Qwen3.5-27B (FP8) | bare | 101 | 48 | 1 |
| Qwen3.5-27B (FP8) | full harness | 80 | 20 | 50 |
| GPT-4 Turbo, FinanceBench paper, single store (human labels) | | 75 | 17 | 58 |

Why the results look like this:

- **The harness trades correct answers for fewer wrong ones.** For 9B it removes 41 wrong answers and gives up 21 correct ones. Most of the lost correct answers failed a code check twice, often over format (a quote not copied exactly, or a division by 1000 inside a formula).
- **A bigger model gets more right in every setting**, because it reads tables better and passes the format checks more often. With the harness, 27B has 8 more correct answers than 9B and 4 more wrong ones. 27B passes the checks on more questions (106 against 97), so more of its mistakes reach the verifier, which catches only about a quarter of them. On the 99 held-out test questions alone, 27B is ahead on both counts (54 correct, 10 wrong, against 46 and 11).
- **2B makes almost no wrong answers with the harness, because it answers almost nothing** (14 of 150). It fails the checks or reports "not found" on the rest.

### Experiment 2: the system must find the document

The same 150 questions with the filing name hidden. The system first picks the filing (a router LLM names company, year and type; code filters the 363 filings to up to 3 candidates), then reads it. This tests **finding plus reading**. The FinanceBench paper calls this the "shared store" setting.

| Model (finds and reads) | Correct | Wrong | Refused | Same model, filing given (experiment 1) | LLM calls per question |
|---|---|---|---|---|---|
| Qwen3.5-9B | 59 | 20 | 71 | 72 / 16 / 62 | 5.5 |
| Qwen3.5-27B (FP8) | 76 | 16 | 58 | 80 / 20 / 50 | 6.4 |
| GPT-4 Turbo, FinanceBench paper, shared store (human labels) | 29 | 20 | 101 | 75 / 17 / 58 | n/a |

Why the results look like this:

- **Finding the filing cost 9B much more than 27B.** 9B lost 13 correct answers (72 to 59) and gained 4 wrong ones. 27B lost only 4 correct answers (80 to 76). Experiment 3 shows why: the router is not the problem, the reader is.
- **A likely reason:** with 2 or 3 candidate filings, the reading gets harder. A later filing repeats last year's numbers as a comparison column, so the reader must pick the right column in a filing that is not the one the question was written for. 27B copes with this better than 9B.
- **27B also had 4 fewer wrong answers** (20 to 16). Of 27B's 20 wrong answers in experiment 1, 7 became refusals and 2 became correct. 5 new wrong answers appeared. When candidate filings disagree, the system returns AMBIGUOUS instead of choosing: this happened on 14 questions, and it cost 10 answers that were correct in experiment 1.
- **It costs more calls:** one router call, then the full pipeline and the verifier on each candidate filing (about 2 per question). Searching the best-ranked filing first and stopping when it answers would bring this close to 4 calls.
- GPT-4 Turbo in the paper's matching setup got 29 correct answers. The paper used human graders and we used a model judge, so this comparison is approximate.

### Experiment 3: which job needs the bigger model, finding or reading?

In experiment 2 one model does two jobs: the **router** picks the filing (one short call), and the **reader** reads the pages and answers (the long calls). This experiment gives the two jobs different models.

**Router alone**, scored against the known correct filing:

| Router | Right company | Right filing among candidates | Right filing ranked first | Candidates per question |
|---|---|---|---|---|
| 9B | 142 / 150 | 124 / 150 | 119 / 150 | 1.95 |
| 27B | 147 / 150 | 130 / 150 | 118 / 150 | 2.22 |

**Router and reader combined** (full harness, filing not given):

| | 9B reads | 27B reads |
|---|---|---|
| **9B picks the filing** | 59 correct, 20 wrong, 71 refused | not run |
| **27B picks the filing** | 58 correct, 20 wrong, 72 refused | 76 correct, 16 wrong, 58 refused |

Reading the grid: the same row with a different reader shows what a bigger reader buys. The same column with a different router shows what a bigger router buys.

Why the router results look like this:

- **Picking the filing is easy for both sizes.** It is a choice of 1 name out of 42, plus a year. 9B ranks the right filing first as often as 27B (119 against 118). It misses a few more company names (142 against 147).
- **Most router misses are not reasoning errors.** In most of the 20 cases where 27B missed the right filing, the question does not say which kind of document it means. For example, "Ulta Beauty's FY2023 results" is answered in the dataset from the Q4 earnings release, while the router picked the 10-K, which contains the same numbers. A bigger router cannot fix missing information. Asking the user can.
- **The grid confirms it: reading needs the bigger model, finding does not.**
  - Same router (27B), bigger reader: 58 to 76 correct, 20 to 16 wrong. On 23 questions only the 27B reader was right.
  - Same reader (9B), bigger router: 59 to 58 correct, 20 to 20 wrong. No difference.
  - This matches experiment 1, where perfect pages gave 27B 12 more correct answers and 9B only 1: the reading step is where size matters.
- **Practical consequence:** a small model can pick the filing, and the large model is needed only for the reading calls. The router is one short call, so the saving is small, but the large model can be kept for the step that benefits from it.

### Latency benchmark

20 dev questions, filing given, full harness. "Single" sends one question at a time to an idle GPU. "Batch" sends all 20 at once. Each model ran on half of an RTX PRO 6000 Blackwell (a 47 GB MIG partition), with the Gemma verifier on a second partition. Source: [`runs/bench/`](runs/bench/), [`finqa/bench.py`](finqa/bench.py).

| Stage, single question (median) | 9B | 27B (FP8) |
|---|---|---|
| Retrieval (BM25 + embeddings) | 0.07 s | 0.04 s |
| Call 1: time to first token | 1.2 s | 2.0 s |
| **Call 1: full JSON output** | **13.1 s** | **44.1 s** |
| Code checks and Python arithmetic | 0.005 s | 0.007 s |
| Call 2: write the answer | 2.9 s | 3.5 s |
| Verifier (Gemma 4 12B) | 1.9 s | 1.9 s |
| **Total** (90th percentile) | **18 s** (26 s) | **48 s** (69 s) |

| Batch of 20 | 9B | 27B (FP8) |
|---|---|---|
| Median time per question | 24 s | 184 s |
| Throughput | about 1,380 questions per hour | about 230 questions per hour |

Why the results look like this:

- **Call 1 is almost all of the time.** It writes about 500 tokens of JSON (values, quotes, formula, and a free-text reason). On these partitions the models write about 45 tokens per second (9B) and 25 (27B). Retrieval and the code checks take milliseconds.
- **Retries repeat call 1.** A failed check sends the whole call again, which is why the 90th percentile is much higher than the median.
- **27B saturates in batch.** Its 31 GB of weights leave little memory on a 47 GB partition for 20 long prompts at once (about 11,000 prompt tokens each), so requests wait in line. 9B has room and keeps its speed.
- **Ways to cut the wait:** a shorter call 1 output (drop the free-text reason when values are found), fewer retries (a more tolerant quote check), showing progress to the user while the pipeline runs, and faster GPUs (a full H100 writes about 2 to 4 times faster than a MIG partition, an estimate not measured here).

## Bare model against full harness

Both settings use the same model and the same retrieved pages. Only the work around the model differs.

- **Bare:** question + 12 pages → model → answer. Nothing checks the answer.
- **Full harness:** the model must list each value with its page and exact quote. Code checks every quote, Python does the arithmetic, code checks every number in the answer, and a second model (Gemma 4 12B) checks the cited page images. If any check fails, the system refuses and gives the reason.

The difference between the two rows of a model shows what the checks add, apart from how good the model is.

## Who refuses: the model or the harness

| Model, full harness | Refused | The model itself said "not found" | Harness code (a check failed twice) | Verifier (Gemma) |
|---|---|---|---|---|
| 2B | 136 | 70 | 62 | 4 |
| 9B | 62 | 18 | 35 | 9 |
| 27B | 50 | 14 | 30 | 5 |

Most refusals come from the harness. A smaller model fails the format checks more often, so it refuses more. That is also why 9B has fewer wrong answers than 27B: some questions that 27B answered wrongly, 9B never got past the checks.

## How it works

![System flow: each stage, its technology, and the decision behind it](docs/diagrams/system-flow.svg)

Each stage is on the left with its technology, and the decision behind it is on the right. Red marks where the system refuses. Generated by [`docs/diagrams/system_flow.py`](docs/diagrams/system_flow.py).

1. **Index (once).** PyMuPDF reads every page twice: plain text for search, layout text (columns joined with `|`) for the model to read. One chunk is one PDF page. Pages whose title is a primary financial statement form a "statement pack" for each filing.
2. **Retrieve.** For the filing: the statement pack, the top BM25 pages and the top pages by embedding similarity (Qwen3-Embedding-8B), at most 12 pages.
3. **Call 1: extract.** The model returns JSON (schema enforced by vLLM): each value with page, exact quote, column, period and scale, plus a formula over value names.
4. **Code checks and Python.** G3: the quote is on the page and the value is in the quote. G5: the formula uses only value names and avg, sum, cagr, abs, max, min. Python computes.
5. **Call 2: answer.** Plain text citing `[v1]`. G4: every number must be a checked value or the computed result.
6. **Verifier.** Gemma 4 12B checks period, unit, column and support on images of the cited pages.
7. **Output.** ANSWER with provenance attached by code, or NOT_FOUND / AMBIGUOUS with the reason.

A failed check gets one retry with the error list, then NOT_FOUND. With no filing named (Path B), a router picks up to 3 candidate filings, each runs separately, and disagreement gives AMBIGUOUS.

### Inside the harness

![Harness data flow: data at each step, the rule each check enforces, retry and refusal paths](docs/diagrams/harness-detail.svg)

The data at each step, the rule each check enforces, and where a failure goes. Generated by [`docs/diagrams/harness_detail.py`](docs/diagrams/harness_detail.py).

Every design decision, with its evidence and what happens if it is wrong, is in [`docs/assumptions.md`](docs/assumptions.md) (A1 to A24). The run log is in [`docs/IMPLEMENTATION.md`](docs/IMPLEMENTATION.md).

## Evaluation method

- **Split.** 51 dev questions for all tuning, 99 test questions run once with the frozen harness ([`eval/split.json`](eval/split.json), stratified by question type, seed 0).
- **Labels.** Correct, wrong or refused, reported as three counts.
- **Grading.** If the gold answer is a number, code checks it at the gold answer's precision (trailing zeros carry no precision: "$8.70" means 8.7), with unit conversion. Otherwise gpt-oss-20b compares the answer with the gold answer and its justification. The pipeline never sees gold data, and a test checks this.
- **Judge calibration.** On the paper's 2,400 human-labeled answers, gpt-oss-20b agrees with the humans 77% of the time. It calls a wrong answer correct 5.9% of the time and a correct answer wrong 12.8% of the time. gpt-oss-120b, for reference: 80%, 5.9%, 11.5%.
- **Unanswerable set.** 290 questions: each question paired with another company's filing (150), or with its year shifted outside the filing (140). The correct output is always a refusal. Every answer on this set, bare or full, goes through the same refusal classifier, so an answer that only says "this filing is about another company" counts as a refusal.

## Detailed results

All numbers come from `python -m finqa.evals.tables` ([`results/tables.md`](results/tables.md), [`results/summary.json`](results/summary.json)). Nothing is typed by hand.

### Every setting of experiment 1 (150 questions, filing named)

"Oracle" gives the model the gold pages instead of retrieved ones. It is a control that measures what retrieval costs. "Glossary" adds financial definitions to the prompt.

| Model | Setting | Correct | Wrong | Refused | Test only (99): correct / wrong / refused | Cited page is a gold page |
|---|---|---|---|---|---|---|
| 2B | bare | 77 | 72 | 1 | 54 / 44 / 1 | n/a |
| 2B | full | 12 | 2 | 136 | 7 / 1 / 91 | 11 of 14 |
| 2B | full + glossary | 12 | 0 | 138 | 8 / 0 / 91 | 10 of 12 |
| 2B | oracle pages | 15 | 4 | 131 | 9 / 3 / 87 | 19 of 19 |
| 9B | bare | 93 | 57 | 0 | 63 / 36 / 0 | n/a |
| 9B | full | 72 | 16 | 62 | 46 / 11 / 42 | 74 of 88 |
| 9B | full + glossary | 62 | 16 | 72 | 40 / 12 / 47 | 67 of 78 |
| 9B | oracle pages | 73 | 17 | 60 | 50 / 11 / 38 | 90 of 90 |
| 27B (FP8) | bare | 101 | 48 | 1 | 67 / 31 / 1 | n/a |
| 27B (FP8) | full | 80 | 20 | 50 | 54 / 10 / 35 | 86 of 101 |
| 27B (FP8) | oracle pages | 92 | 13 | 45 | 59 / 7 / 33 | 107 of 107 |

The glossary was not run for 27B, because it lowered coverage for 2B and 9B without reducing wrong answers.

### Questions with no answer in the filing (290 per model)

| Model | Bare: false answers | Full harness: false answers |
|---|---|---|
| 2B | 53 | 0 |
| 9B | 20 | 0 |
| 27B (FP8) | 22 | 1 |

### Size ladder

| | 2B | 9B | 27B (FP8) |
|---|---|---|---|
| Pass all code checks (reach the verifier) | 18 | 97 | 106 |
| Gain from gold pages, full harness (correct) | +3 | +1 | +12 |
| LLM seconds per question, full harness | 21 | 59 | 190 |

- A bigger model passes the checks more often, so it answers more.
- Gold pages help 27B a lot (+12 correct) and 9B hardly at all (+1). 9B loses its answers at reading and checking, so better pages do not help it. 27B can use better pages.

### Verifier (Gemma 4 12B) against the judge

Answers that passed every code check, before the verifier. "Let through" = the verifier accepted a wrong answer.

| Run | Checked | Accepted, correct | Accepted, wrong (let through) | Rejected, correct (lost) | Rejected, wrong (caught) |
|---|---|---|---|---|---|
| 2B full | 18 | 12 | 2 | 1 | 3 |
| 9B full | 97 | 70 | 18 | 2 | 7 |
| 27B full | 106 | 82 | 19 | 1 | 4 |
| 27B Path B (per candidate filing) | 165 | 127 | 27 | 1 | 10 |

The verifier rarely rejects a correct answer, but it lets most wrong answers through: it caught 7 of 25 for 9B and 4 of 23 for 27B. It is smaller than the 27B model it checks.

### Retrieval (dev, 51 questions, 12-page budget)

| Option | Gold page found |
|---|---|
| Statement pack + BM25 | 84% |
| **+ dense embeddings (used)** | **87%** |
| + LLM query planning | 87% |
| All of the above | 90% |

Rule fixed before the results: take the cheapest option within 5 points of the best.

### FinanceBench paper baselines (human labels, same 150 questions)

| Paper configuration | Correct | Wrong | Refused |
|---|---|---|---|
| GPT-4 Turbo, gold pages | 128 | 22 | 0 |
| GPT-4 Turbo, single store | 75 | 17 | 58 |
| GPT-4 Turbo, shared store | 29 | 20 | 101 |
| GPT-4, single store | 63 | 16 | 71 |
| Llama 2, single store | 62 | 81 | 7 |

## What worked

- **Checks between the model and the user.** For every size, the harness cut wrong answers sharply, and false answers on unanswerable questions fell to 0 or 1.
- **Code does the arithmetic and attaches the provenance.** Every answer cites a quote that exists on its page. When the filing is named, every answer cites that filing.
- **The statement pack.** Most evidence is on the three primary statements. Always showing those pages gave 84% recall before any learned retrieval.
- **Rules written before the results, and a held-out test set.** Test-only numbers track the full-set numbers, so tuning on dev did not overfit.
- **Routing without a named filing.** With 27B, Path B lost only 4 correct answers against Path A.

## What did not work

- **The verifier.** It catches about a quarter of the wrong answers that pass the code checks.
- **Definitions.** Most remaining wrong answers use a real, correctly cited number for a different definition of the metric: working capital from total instead of operating items, a different quick ratio, capex/revenue instead of assets/revenue. No check catches this, and a glossary in the prompt did not help.
- **Small models and strict checks.** 2B refuses 91% of questions. Its few answers are right, but it is not usable.
- **9B loses answers to format errors.** It fails code checks twice on 35 questions, for example by putting `/1000` in a formula or copying a quote inexactly.

## What would change the choice of model

- **Experiment 3 splits the work:** a small model is enough to pick the filing, while reading the filing and answering benefits from the larger model (18 more correct answers with the same router).

- **If a wrong answer is far worse than a refusal:** 9B or 27B with the harness, plus a stronger verifier. 9B has slightly fewer wrong answers on the full set. 27B has more correct answers and is ahead on the held-out test set.
- **If coverage matters more:** 27B, which gets the most correct answers in every setting.
- **If cost matters:** 9B, which is about 3 times faster per question than 27B.
- **What to fix first, for any model:** a stronger verifier that also checks the formula against the question, and a way to show which definition of a metric the answer used.

## Limitations and compute

The work ran on Georgia Tech PACE ICE with a student allocation. 80 GB GPUs waited in the queue for more than a day, so:

- **27B ran in FP8** (`Qwen/Qwen3.5-27B-FP8`, 31 GB), on one 47 GB Blackwell partition. bf16 (52 GB) did not fit, and the partitions cannot be joined. FP8 is usually very close to bf16, but not identical.
- **A smaller verifier and judge:** Gemma 4 12B instead of a 27B verifier, gpt-oss-20b instead of gpt-oss-120b. The judge's calibration is above.
- **One run per configuration,** temperature 0. No variance across seeds.
- **Dev round 2 fixes were tested on 2B and 9B only,** because 27B could not get a GPU at that time.

With more compute: 27B in bf16 and larger models, a larger verifier with reasoning, the 120b judge, Path B for every size, and several seeds. Each model is one setting in the job script, so the harness does not change.

## Reproduce

```bash
scripts/fetch_data.sh                    # FinanceBench clone into data/
python -m finqa.cli embed                # page vectors (GPU)
./pace/submit.sh final                   # pass 1 for each run, on ICE (see pace/)
# verifier and judge: pace/job.sbatch with MODEL=google/gemma-4-12B-it / openai/gpt-oss-20b
python -m finqa.evals.judge regrade      # re-apply the code grading rule to existing judge files
python -m finqa.evals.publish --main all-9b-full --runs ...
python -m finqa.evals.tables > results/tables.md
python -m finqa.evals.viewer             # rebuild the demo data
pytest -q
```

Code layout: `finqa/` (pipeline: parse, retrieve, answer, checks, formula, verify), `finqa/evals/` (judge, metrics, tables, viewer, the only code that reads gold data), `pace/` (Slurm and vLLM scripts), `runs/` (every model output, JSONL).
