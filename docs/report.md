---
title: "Financial Document QA on FinanceBench"
---

Live demo: finqa-demo.vercel.app (step-by-step replay on sample questions, and every answer with its cited pages). Code and full results: github.com/moriowen/finqa. The system diagram is on page 3.

This is a comparative experiment, not a product. It compares Qwen3.5 at 2B, 9B and 27B, each with and without a checking pipeline, to decide which model and setup to use later. One rule shaped the design: a wrong answer is worse than no answer. If a configuration cannot point to evidence that code has checked, it refuses and gives the reason. Every configuration is reported as three counts: correct, wrong and refused.

## 1. System design

**Parsing.** PyMuPDF reads each of the 363 filings and stores every page twice: plain text for search, and layout text that keeps table rows and columns (joined with "|") for the model to read. One chunk is one PDF page, so tables stay whole and the page number is the provenance. At index time, code marks the pages whose title is a primary statement (income statement, balance sheet, cash flow statement). These pages are called the statement pack, because most gold evidence is on them.

**Retrieval.** Code, not the model, picks the pages: the statement pack, the top BM25 pages and the top pages by embedding similarity (Qwen3-Embedding-8B), about 12 pages. This finds a gold page for 87% of the dev questions. Four retrieval options were compared on the dev questions, with a selection rule written down before the results.

**Generation.** Three LLM calls, with Python checks between them.

1. Call 1 (answering model) returns JSON, with the schema enforced by vLLM: each value it needs, with page, exact quote, column, period and unit, plus a formula over value names. It writes no answer yet.
2. Python checks that each quote is on its page and contains the value, and that the formula uses only value names and six functions. Python then does the arithmetic.
3. Call 2 (same model) sees only the checked values and the result, and writes the answer, citing values as [v1]. Python checks that every number in it is a checked value or the result.
4. Call 3 is a verifier from another model family (Gemma 4 12B). It looks at images of the cited pages and confirms period, unit, column and support.
5. Code attaches the provenance (filing, page, quote, passage). The model never writes a page number.

A failed check gets one retry with the error list, then a refusal. When no filing is named, a router picks up to three candidate filings, each runs the same pipeline, and disagreement returns AMBIGUOUS. "Bare" is the comparison setting: the same model and pages in one prompt, with no checks.

Models ran with vLLM on Georgia Tech's ICE cluster. The pipeline was tuned on 51 dev questions, and the other 99 were run once at the end. Numeric answers were graded by code at the gold answer's precision. Text answers were graded by gpt-oss-20b, which agreed with the FinanceBench paper's 2,400 human labels 77% of the time.

## 2. Answers with provenance

Every answer and refusal of every configuration, with page, quote, passage and an image of the cited page, is in the demo and in the repository's results folder. Totals over the 150 questions:

| Configuration | Correct | Wrong | Refused |
|---|---|---|---|
| 2B, bare | 77 | 72 | 1 |
| 2B, full pipeline | 12 | 2 | 136 |
| 9B, bare | 93 | 57 | 0 |
| 9B, full pipeline | 72 | 16 | 62 |
| 27B (FP8), bare | 101 | 48 | 1 |
| 27B (FP8), full pipeline | 80 | 20 | 50 |
| 27B (FP8), full pipeline, no filing named | 76 | 16 | 58 |
| GPT-4 Turbo, paper, single store (human labels) | 75 | 17 | 58 |
| GPT-4 Turbo, paper, shared store, no filing named | 29 | 20 | 101 |

Three rows from the 9B answer file:

- *Which of JPM's segments had the highest net income in 2022 Q2?* Corporate & Investment Bank, $3,725 million, computed as the max of four segment values. Evidence: JPMORGAN_2022Q2_10Q, page 27, "Net income | $3,725", plus pages 22, 33 and 37 for the other segments.
- *Does American Water Works have positive working capital in FY2022?* No: $1,250 million current assets minus $2,811 million current liabilities is -$1,561 million. Evidence: AMERICANWATERWORKS_2022_10K, page 81 "Total current assets | 1,250" and page 82 "Total current liabilities | 2,811".
- *Is Verizon's liquidity healthy based on its quick ratio for FY2022?* Refused. Reason: the model found the inputs on page 56 but could not tell which items the quick ratio should include.

## 3. What worked, what didn't, and what would change

**What worked.** The checks. For every size they cut wrong answers sharply (9B: 57 to 16), at the cost of correct answers (93 to 72). On 290 questions paired with a filing that holds no answer, the full pipeline gave 0 false answers with 2B and 9B and 1 with 27B. Without the checks the same models gave 53, 20 and 22. Without a named filing, 27B got 76 right, against 29 for GPT-4 Turbo in the paper's matching setup (the graders differ, so this is approximate). Because code does the arithmetic and attaches the citations, no answer can cite text that is not on its page.

**What didn't.** The verifier caught only about a quarter of the wrong answers that passed the code checks (7 of 25 for 9B, 4 of 23 for 27B). Most remaining errors use a real, correctly cited number for a different definition of the metric, such as working capital from total instead of operating items. A glossary in the prompt did not help. Size cuts both ways: 27B gets the most correct answers in every setting, but it also passes the checks more often, so more of its errors reach the weak verifier. With the full pipeline it has 4 more wrong answers than 9B on all 150 questions, and 1 fewer on the 99 held-out ones. Most refusals come from the checks, not the model: 9B fails a check twice on 35 questions, often over format, such as dividing by 1000 in a formula. 2B refuses 91% of questions.

**What would change, and how to choose the model.** For any model: a verifier that also checks the formula against the question, and an answer that states which definition of a metric it used. For the choice: if wrong answers must be rare, 9B or 27B with the pipeline and a stronger verifier. If coverage matters more, 27B. If cost matters, 9B, which is about 3 times faster. Compute limited the runs: 80 GB GPUs were not available, so 27B ran in FP8, the verifier was a 12B model, the judge a 20B model, and each configuration ran once. With more compute, the next step would be full-precision and larger models, a larger verifier and judge, and several runs per configuration.

```{=html}
<div class="figure-page">
```
![](diagrams/system-flow.svg)
```{=html}
</div>
```
