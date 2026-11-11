# FinanceBench QA with provenance: write-up

Code, full results and all 150 answers with provenance: **https://github.com/moriowen/finqa** (README, and `results/answers.md`).

## Goal

The system answers questions about SEC filings and returns the PDF page, the quote and the passage behind each answer. I set one priority before the design work: a wrong answer is worse than no answer. If the system cannot point to checked evidence, it returns NOT_FOUND with the reason. I measure success by the **wrong-answer rate** first and coverage second.

## System design

The design separates what the model is good at (reading a page, choosing values) from what code does reliably (finding text, arithmetic, attaching citations).

1. **Parsing.** PyMuPDF stores each page twice: plain text for search, and layout text that keeps table rows and columns for the model to read. Pages whose title is a primary statement (income statement, balance sheet, cash flows) form a per-filing **statement pack**. Data analysis of the gold evidence showed that most answers sit on those pages.
2. **Retrieval.** Statement pack + BM25 + dense embeddings (Qwen3-Embedding-8B) over the given filing, at most 12 pages. On the dev set this reaches 87% gold-page recall. I compared four retrieval options on dev with a decision rule written before the results.
3. **Extraction (LLM call 1).** JSON enforced by the server: each value with its page, exact quote, column, period and scale, and a formula over value names.
4. **Code checks.** The quote must be on the page and contain the value. The formula may use only value names and a few functions. **Python does the arithmetic.**
5. **Answer (LLM call 2).** Plain text that cites `[v1]`. Every number in it must be a checked value or the computed result.
6. **Verifier.** A model from another family (Gemma 4 12B) sees images of the cited pages and must confirm period, unit, column and support.
7. **Output.** Code attaches the provenance from the checked values. The model never writes a page number. Each row also names the answering model and the verifier.

Any failed check gets one retry with the error message, then NOT_FOUND. A second path, for questions with no filing named, routes to up to 3 candidate filings and returns AMBIGUOUS if they disagree. It is built but not evaluated.

Every decision is recorded with its evidence and "what changes if this is wrong" in `docs/assumptions.md` (23 entries).

## Evaluation

- 51 dev questions for all tuning; 99 test questions run once with the frozen system.
- Numeric answers are graded by code. The others are graded by an LLM judge (gpt-oss-20b), which I first calibrated on the paper's 2,400 human-labeled answers (76% agreement; it calls a wrong answer correct 5% of the time).
- 290 extra questions with no answer in the filing (wrong filing, or year shifted) test whether the system refuses.
- To separate the model from the harness, each Qwen3.5 size ran three ways: **bare** (same pages, one prompt), **full** harness, and **oracle** (gold pages).

## Results (150 questions)

| Setup | Correct | Wrong | Refused | Wrong-answer rate |
|---|---|---|---|---|
| Qwen3.5-9B bare | 91 | 59 | 0 | 39% |
| **Qwen3.5-9B full harness (official)** | **71** | **17** | **62** | **11%** |
| Qwen3.5-9B full, gold pages | 71 | 19 | 60 | 13% |
| Qwen3.5-2B bare | 73 | 76 | 1 | 51% |
| Qwen3.5-2B full harness | 12 | 2 | 136 | 1% |
| GPT-4 Turbo, paper, single store (human labels) | 75 | 17 | 58 | 11% |

- **Unanswerable questions:** 9B full gave 1 false answer out of 290 (bare: 20). 2B full gave 0 (bare: 53).
- **Provenance:** every 9B answer cites the right filing, and 84% cite a gold evidence page.
- **Held-out test only:** 9B full is 12% wrong, close to the full-set 11%, so tuning on dev did not overfit.

## What worked

- **The harness, more than the model size.** It cut 9B wrong answers by 71% (59 to 17). A local 9B model reaches the same wrong-answer rate and coverage as GPT-4 Turbo in the paper's comparable setup. The judges differ, so this comparison is approximate.
- **Code for arithmetic and citations.** No answer can cite a quote that is not on its page.
- **Refusals.** The checks almost never let an answer through when the filing has none.

## What did not work

- **Retrieval was not the limit.** Gold pages give the same 71 correct. The losses happen after retrieval: 35 questions fail a code check twice, and 18 more find no evidence.
- **Definitions cause most of the remaining wrong answers.** Examples: working capital from total instead of operating items, a different quick ratio, capex/revenue instead of assets/revenue. The numbers are real and correctly cited, so neither the code checks nor the verifier catch them. A glossary of definitions in the prompt did not help (coverage 59% to 52%, same wrong count).
- **The verifier is weak.** It caught 8 of 26 wrong 9B answers that passed the code checks, and lost 1 correct answer.
- **2B is too small for strict checks.** Its answers are almost always right, but it answers only 9% of questions.

## What I would change

1. **Show the definition.** When a metric has several common definitions, state the one used or ask the user. This targets the largest group of remaining errors.
2. **Verify the formula against the question,** not only the values against the page.
3. **Recover check failures** with a further retry or a larger model only on retry.
4. **Evaluate Path B** (no filing named).

## Limitations and future scope

The work ran on a student GPU allocation. The 80 GB GPUs stayed in the queue for more than a day, so the final runs used 47 GB GPUs: no 27B answering model, Gemma 4 12B instead of a 27B verifier, and gpt-oss-20b instead of the 120b judge. All runs use one seed. With more compute, I would run 27B and larger answering models, a stronger verifier with reasoning, the larger judge, Path B, and several seeds. The pipeline needs no change for any of these: each model is one setting in the job script.
