---
title: "Financial Document QA on FinanceBench"
---

Live demo: finqa-demo.vercel.app (step-by-step replay on sample questions, and every answer with its cited pages). Code and full results: github.com/moriowen/finqa. The system diagram is on page 3.

This is a comparative experiment, not a product. Qwen3.5 at 9B and 27B (and 2B in the first experiment) were compared with and without a checking pipeline, to decide which model and setup to use later. One rule shaped the design: a wrong answer is worse than no answer. If a configuration cannot point to evidence that code has checked, it refuses and gives the reason. Results are reported as three counts out of 150 questions: correct, wrong and refused.

**Terms used**

| Term | Meaning |
|---|---|
| Bare | The model gets the question and the retrieved pages in one prompt and answers. Nothing checks it. |
| Full pipeline | The same model and pages inside the checking pipeline of section 1. Any failed check ends in a refusal. |
| Refused | No answer is given (NOT_FOUND or AMBIGUOUS), with the reason. Counted apart from wrong answers. |
| Provenance | The filing, PDF page, exact quote and surrounding passage behind each value in an answer. |
| Router, reader | Router: the LLM call that picks the filing when none is named. Reader: the calls that read the pages and answer. |
| Statement pack | The primary statement pages of a filing: income statement, balance sheet, cash flow statement. |
| BM25, embedding search | BM25 ranks pages by the question's words, rare words counting more. Embedding search ranks them by similarity of meaning. |
| Gold answer, gold page | The answer and evidence page written by FinanceBench's analysts. Used only for grading. |

## 1. System design

**Parsing.** PyMuPDF reads each of the 363 filings and stores every page twice: plain text for search, and layout text that keeps table rows and columns for the model to read. One chunk is one PDF page, so tables stay whole and the page number is the provenance. Pages whose title is a primary statement form the statement pack, because most gold evidence is on them.

**Retrieval.** Code, not the model, picks about 12 pages from the filing: the statement pack plus the best pages from BM25 and from embedding search (Qwen3-Embedding-8B), merged by rank. This finds a gold page for 87% of the dev questions. When no filing is named, a router call first names the company, year and type, and code narrows the 363 filings to up to three candidates.

**Generation.** Three LLM calls, with Python checks between them. (1) The reader returns JSON, with the schema enforced by vLLM: each value with page, exact quote, column and period, plus a formula over value names. (2) Python checks that each quote is on its page and holds the value, checks the formula, and does the arithmetic. (3) The reader writes the answer from the checked values only, and Python checks every number in it. (4) A verifier from another model family (Gemma 4 12B) checks period, unit, column and support on images of the cited pages. Code then attaches the provenance. A failed check gets one retry, then a refusal. Candidate filings that disagree return AMBIGUOUS.

The pipeline was tuned on 51 dev questions, and the other 99 were run once at the end. Numeric answers were graded by code, text answers by gpt-oss-20b, which agreed with the FinanceBench paper's 2,400 human labels 77% of the time.

## 2. Answers with provenance

Every answer and refusal of every configuration, with page, quote, passage and an image of the page, is in the demo and the repository's results folder.

**Experiment 1: the filing is given** (tests reading)

| Configuration | Correct | Wrong | Refused |
|---|---|---|---|
| 9B, bare | 93 | 57 | 0 |
| 9B, full pipeline | 72 | 16 | 62 |
| 27B (FP8), bare | 101 | 48 | 1 |
| 27B (FP8), full pipeline | 80 | 20 | 50 |
| GPT-4 Turbo, paper, single store (human labels) | 75 | 17 | 58 |

2B answered only 14 questions with the full pipeline (12 correct) and was not used further. On 290 extra questions whose filing holds no answer, the full pipeline gave 0 false answers with 9B and 1 with 27B. The same models without checks gave 20 and 22.

**Experiments 2 and 3: the system must find the filing** (tests finding and reading, and which of the two needs the larger model)

| Finds the filing | Reads | Correct | Wrong | Refused |
|---|---|---|---|---|
| 9B | 9B | 59 | 20 | 71 |
| 27B | 9B | 58 | 20 | 72 |
| 27B | 27B | 76 | 16 | 58 |
| GPT-4 Turbo, paper, shared store (human labels) | | 29 | 20 | 101 |

Two sample answers from 9B, and one refusal:

- *Which of JPM's segments had the highest net income in 2022 Q2?* Corporate & Investment Bank, $3,725 million, the max of four segment values. Evidence: JPMORGAN_2022Q2_10Q, page 27, "Net income | $3,725", with pages 22, 33 and 37 for the other segments.
- *Does American Water Works have positive working capital in FY2022?* No: $1,250 million minus $2,811 million is -$1,561 million. Evidence: AMERICANWATERWORKS_2022_10K, pages 81 and 82.
- *Is Verizon's liquidity healthy based on its quick ratio for FY2022?* Refused: the inputs were found on page 56, but not which items the quick ratio should include.

## 3. What worked, what didn't, and what would change

**What worked.** The checks did more than model size to prevent wrong answers: they cut wrong answers by more than half for each model (9B: 57 to 16, 27B: 48 to 20) and almost removed false answers on questions with no answer, at the cost of turning some correct answers into refusals. Letting code do the arithmetic and attach the citations means no answer can cite text that is not on its page. Finding the filing works with a small model: the 9B and 27B routers rank the right filing first equally often (119 and 118 of 150), and swapping the router made no difference to the answers. Most router misses come from questions that do not say which document they mean, which calls for asking the user, not for a larger model.

**What didn't.** Reading is where size matters. With the same router, the 27B reader got 18 more correct answers than 9B and 4 fewer wrong ones, so finding the filing cost 9B 13 correct answers but 27B only 4. With the filing given, 27B gets more correct answers but also 4 more wrong ones than 9B, because it passes the code checks more often and the verifier catches only about a quarter of the wrong answers that reach it. Most remaining errors use a real, correctly cited number for a different definition of the metric, such as working capital from total instead of operating items, which no check catches. Speed: one question takes 18 s with 9B and 48 s with 27B, and almost all of it is the first call writing its JSON. Retrieval and the checks take milliseconds.

**What would change.** A small model to find the filing and the larger model to read it. A verifier that also checks the formula against the question, and answers that state which definition of a metric they used. Searching the best-ranked filing first and stopping when it answers, instead of reading every candidate. A shorter first-call output and fewer retries to cut the wait. Limited compute meant 27B in FP8, a 12B verifier, a 20B judge and one run each. More compute would allow larger models, verifier and judge, and repeated runs.

```{=html}
<div class="figure-page">
```
![](diagrams/system-flow.svg)
```{=html}
</div>
```
