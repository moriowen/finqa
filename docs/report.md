---
title: "Financial Document QA on FinanceBench"
---

[Live demo](https://finqa-demo.vercel.app) · [All 150 answers, 9B](https://github.com/moriowen/finqa/blob/main/results/answers.md) · [Code and full results](https://github.com/moriowen/finqa) · System diagram on page 3

This system answers questions about financial filings and cites the pages it used. When it cannot verify an answer, it refuses and gives the reason. The experiments compare a single Qwen3.5 prompt (*bare*) with a version that checks the evidence before it answers (*full pipeline*). With the filing supplied, the checks cut wrong answers from 57 to 16 for 9B and from 48 to 20 for 27B. Both models refused more often.

```{=html}
<table class="models">
<thead><tr><th>Role</th><th>Model</th><th>Why this model</th></tr></thead>
<tbody>
<tr><td>Router and reader</td><td>Qwen3.5 9B and 27B (FP8)</td><td>Same family at both sizes, with 27B in FP8 to fit the available GPUs. 2B gave only 14 answers with checks and left after Experiment 1.</td></tr>
<tr><td>Verifier</td><td>Gemma 4 12B</td><td>Reads page images and fits the free GPUs.</td></tr>
<tr><td>Grader</td><td>gpt-oss-20b</td><td>Fits the free GPUs. Agrees with 77% of the paper's human labels.</td></tr>
</tbody>
</table>
```

## 1. System design

**Parsing.** In the 189 FinanceBench evidence items, 69% are tables, and a question's evidence fills about half a page. So each PDF page is one chunk: it keeps a whole table, is about twice the size of the evidence, and gives the page number to cite. PyMuPDF stores plain text for search and column-preserving layout text for the model.

**Retrieval.** Keyword search alone put an evidence page in the top 5 for only 27% of development questions, because questions name a concept such as "quick ratio" while the evidence page shows only its inputs. Over half of the evidence pages are primary financial statements, so the reader always gets them, plus the best BM25 and embedding matches (about 12 pages). This finds an evidence page for 87% of development questions. LLM query planning also reached 87%, so the cheaper option stayed.

**Generation and checking.** A wrong answer costs more than no answer, so code checks each step a model can get wrong. About 80 of the 150 questions need a computed metric, so Qwen3.5 does no arithmetic: it extracts each value with its page and exact quote and writes a formula over the value names. Python confirms each quote on its page and computes the result. Qwen writes the answer from the checked values, and Python checks its numbers. Text extraction can misplace a column, so Gemma checks the answer against the cited page images. Code attaches the filing, page, quote and passage, so no answer cites a page the model did not read. A failed check gets one retry, then a refusal with its reason.

**Grading.** The accuracy tables cover all 150 questions: 51 for development (17 from each of the three 50-question types, so both sets keep the same mix) and 99 held out until the final run. Code accepted numeric matches, and gpt-oss-20b graded the rest (77% agreement with the paper's 2,400 human labels).

**Experiment 1. FinanceBench supplies the filing**

| Configuration | Correct | Wrong | Refused |
|---|---|---|---|
| 9B, bare | 93 | 57 | 0 |
| 9B, full pipeline | 72 | 16 | 62 |
| 27B (FP8), bare | 101 | 48 | 1 |
| 27B (FP8), full pipeline | 80 | 20 | 50 |
| GPT-4 Turbo, from the paper (human-graded reference) | 75 | 17 | 58 |

**Inference time.** 20 development questions, sent one at a time, with the filing supplied.

| Stage (median, 47 GB Blackwell partition) | 9B | 27B (FP8) |
|---|---|---|
| Call 1: extract values and formula | 13.1 s | 44.1 s |
| Retrieval, Python checks and arithmetic | under 0.1 s | under 0.1 s |
| Call 2: write the answer | 2.9 s | 3.5 s |
| Gemma verifier | 1.9 s | 1.9 s |
| Total (90th percentile) | 18 s (26 s) | 48 s (69 s) |
| Throughput, batch of 20 questions | about 1,380 per hour | about 230 per hour |

## 2. Finding the filing

Without a supplied filing, a router predicts the company, year and filing type. The code uses those predictions to select up to three filings, which the reader checks separately. If the answers disagree, the system returns AMBIGUOUS.

**Experiment 2. One model finds and reads the filing** (full pipeline)

| Model | Correct | Wrong | Refused | Experiment 1 |
|---|---|---|---|---|
| 9B | 59 | 20 | 71 | 72 / 16 / 62 |
| 27B (FP8) | 76 | 16 | 58 | 80 / 20 / 50 |
| GPT-4 Turbo, shared store (human-graded reference) | 29 | 20 | 101 | 75 / 17 / 58 |

Finding the filing cost 9B 13 correct answers and 27B only 4.

**Experiment 3. Which step needs the larger model?** The router (one short call) picks the filing, and the reader (the long calls) answers. This experiment gives them different models. Cells show correct / wrong / refused.

| Router (right filing ranked first) | 9B reader | 27B reader |
|---|---|---|
| 9B (119 of 150) | 59 / 20 / 71 | not run |
| 27B (118 of 150) | 58 / 20 / 72 | 76 / 16 / 58 |

With the reader fixed at 9B, a larger router changed correct answers from 59 to 58. With the router fixed at 27B, a larger reader raised them from 58 to 76. The larger reader produced the bigger gain in this experiment. The next pairing to test is a 9B router with a 27B reader. The 9B router included the reference filing among its candidates on 124 questions, compared with 130 for the 27B router.

## 3. What worked, what didn't, and what to change

**What worked.** The checks cut wrong answers more than the larger model did: from 57 to 16 for 9B, while 27B without checks still gave 48. On 290 questions whose filing holds no answer, they cut false answers from 20 to 0 for 9B and from 22 to 1 for 27B.

**What didn't.** The checks also turned correct answers into refusals (9B: 93 to 72 correct). Most remaining wrong answers cite real numbers but use a different definition of the metric. For Corning, the system cited page 60 and calculated $2,278 million in working capital using all current assets and liabilities. FinanceBench expected $831 million using operating items only. Gemma caught only about a quarter of the wrong answers that reached it.

**What to change.** Each design choice rests on an assumption recorded in [assumptions.md](https://github.com/moriowen/finqa/blob/main/docs/assumptions.md). If an assumption turns out false, or further runs give more evidence about it, the design must change with it.

1. **Fewer wrong answers.** A new check should compare the formula with the metric that the question names. A verifier that reasons before it decides, or agreement across several sampled answers, can catch more errors.
2. **Faster answers.** Call 1 takes most of the time because it writes about 500 tokens of JSON, including a free-text reason. A shorter schema can cut this time, and a retry of only the failed value would cost less than repeating the whole call. Without a supplied filing, a test should read the top-ranked candidate first, stop at the first verified answer, and count how often this misses a disagreement between filings. The pipeline now refuses when filings disagree.
3. **Better models.** GPU memory forced 27B into FP8: bf16 needs 52 GB, and each available GPU partition has 47 GB. Long queues for larger GPUs on PACE ICE set the 12B verifier, the 20B judge and one run per configuration. With more GPU time, the same comparison should run at full precision, with larger models and other model families in each role, and repeat each run to measure variance.

```{=html}
<div class="figure-page">
```
![](diagrams/system-flow.svg)
```{=html}
</div>
```
