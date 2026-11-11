# Architecture assumptions

This is a running list of assumptions that can change the architecture of the system.
For each assumption: what we assume, why, and what changes if the assumption is false.

Status values: **Decided** (we chose it and can defend it), **Open** (not decided yet).

The full architecture and the impact of each assumption change are in [`architecture.md`](architecture.md).

---

## A1. The user may or may not name the filing

- **Status:** Decided (D1, revised 2026-11-11). The system supports both paths.
  - **Path A:** the input is the question + `doc_name`. The system searches only that filing.
  - **Path B:** the input is only the question. The system finds the filing.
- **History:** We first chose Path A only. The reasons were product (an analyst chooses the filing) and measurement (each gold answer is labeled against one `doc_name`). We then decided that the system must also work when the user does not name the filing.
- **Design: one pipeline, with `doc_name` optional.** Path A is Case 1 of the flow below, where the user gives the router's output in advance.

  ```
  question (+ optional doc_name)
    → 1. Router
          doc_name given → candidates = [that filing]            (Path A)
          not given      → extract company, period, doc type
                           → metadata filter → candidate filings  (Path B)
    → 2. Search the pages of the candidates (one shared index + metadata filter)
    → 3. Rank the pages. On a tie, prefer the more recent filing.
    → Answer
    → 4. Conflict check (only possible with 2+ candidates)
  ```

  - **Superseded in part by A20:** steps 2 and 3 do not rank pages across filings. Each candidate filing runs its own pipeline (search, answer, checks), and step 4 compares the results. Reason: statements from different years in one prompt can mix restated numbers.

- **Decisions that follow from supporting Path B:**
  1. **Index all filings** (369: 361 with metadata + 8 parsed from the file name, A20), not only the 84 filings that have questions. An index of only the 84 gives Path B a leak: every candidate would be a filing that has a question.
  2. **The router maps company names to the metadata list.** Questions use "JPM", "JnJ", "Block (formerly known as Square)". The LLM must pick a name from the metadata list and must not invent one.
  3. **Evaluate both paths on the same 150 questions.** The gap between them is the cost of routing. Label each Path B failure:
     - **Routing error:** the gold filing was not in the candidates, or it ranked too low.
     - **True ambiguity:** another filing gave a different answer that is still correct. Review these by hand, because each gold answer is tied to one filing.
  4. **Metrics added for Path B:** routing accuracy (gold filing is the top candidate) and candidate recall (gold filing is in the candidate list).
  5. **Provenance includes `doc_name` + page**, not only the page.
- **Evidence that Path B is not trivial (150 questions, checked 2026-11-11):**
  - 9 questions name no period.
  - 62 questions match more than one filing on company + period (for example, 10-K, 10-Q, and earnings report for the same year).
  - 40 questions name more than one year.
  - 3 questions name a year that is not the filing year (for example, a FY2023 forecast that is in the 2022 10-K).
- **How the 4-step flow handles Path B:** the steps are one flow, not alternatives.
  The system cannot know the case before it searches, so it runs the steps in order.

  | Case | Example | Resolved by |
  |---|---|---|
  | One filing matches | "Key agenda of AMCOR's 8-K dated 1 July 2022" | Step 1 |
  | Many match, same answer in all | "What industry does AMCOR operate in?" | Step 3 (take the most recent) |
  | Many match, only some have the evidence | "FY2017–FY2019 average capex" (only the FY2019 10-K has all 3 years) | Step 2 |
  | Many match, different answers | A restated number, or "Is the dividend trend stable?" | Step 4 |

  1. **Router:** an LLM extracts company, period, and document type from the question. A metadata filter selects the candidate filings.
  2. **Search** the pages of all candidates in a shared index with a metadata filter.
  3. **Rank** pages across the filings. On a tie, prefer the more recent filing (a later filing can restate an earlier number).
  4. **Conflict check:** if evidence from different filings disagrees, return `AMBIGUOUS` with each value and its own provenance (decided by A2 and A20). If A2 is reversed, return the value from the highest-ranked filing and list the others.
  - Steps 2 to 4 are the same code for both paths. Only step 1 differs.

## A2. A wrong answer is worse than no answer

- **Status:** Decided (D2, 2026-11-11). This is the top priority of the system. The user confirmed it as firm: no checked citation → no answer. An abstention row never shows the draft value that failed the checks.
- **Why:** Finance use case. A wrong number that looks correct is worse than "I don't know".
- **Limit we accept:** no system can guarantee zero wrong answers. A system that always abstains has zero wrong answers and is useless. The goal is a trade-off: minimize wrong answers, keep coverage acceptable.
- **Output types:**

  | Output | When | Contains |
  |---|---|---|
  | `ANSWER` | All checks pass | Answer + doc + page + quote for each value |
  | `AMBIGUOUS` | Path B: 2+ filings give different answers | Each candidate filing with its value and provenance |
  | `NOT_FOUND` | No evidence passes the checks | What the system searched, and why it stopped |

- **Guardrails (each layer catches a different failure):**

  | # | Guardrail | Catches | Type |
  |---|---|---|---|
  | 1 | Use only retrieved pages. The prompt permits abstention. | Answers from memory | Prompt |
  | 2 | Each value has a page and an exact quote | Values with no source | Format |
  | 3 | Quote check: the quote exists on the cited page | Invented quotes, wrong pages | Code |
  | 4 | Number check: each number is in a quote, or computed from quoted numbers | Invented numbers | Code |
  | 5 | Arithmetic in code, not in the LLM | Calculation errors | Code |
  | 6 | Period and unit check (year column, millions vs thousands) | Silent finance errors | LLM verifier |
  | 7 | Independent verifier sees only evidence + answer | Wrong reasoning from correct evidence | LLM |
  | 8 | Conflict check across filings | Path B ambiguity | Code + LLM |

  If a check fails: retry once, then return `NOT_FOUND` or `AMBIGUOUS`.

- **Metrics:**
  - Wrong-answer rate = answered and wrong / all questions. Minimize this.
  - Coverage = answered / all questions.
  - Selective accuracy = correct / answered.
  - Report the trade-off curve (coverage vs wrong-answer rate), not one number.
- **Test gap and fix:** in Path A, every FinanceBench question has an answer in its filing, so `NOT_FOUND` is never tested. Add unanswerable questions with no labeling:
  - A real question against the wrong filing (a 3M question against a Boeing 10-K).
  - A real question with the year changed to a year that the filing does not cover.
  - Path B: the 62 questions that match more than one filing test `AMBIGUOUS`.
- **If false (the system must always answer):** drop `NOT_FOUND`. Keep guardrails 3 to 5 as quality checks. Report accuracy only.

## A6. Scale: about 54,000 pages, static

- **Status:** Decided (measured 2026-11-11 with PyMuPDF).
- **Measured:**

  | Set | Files | PDF size | Pages | Text | Tokens (chars / 4) |
  |---|---|---|---|---|---|
  | 84 question filings | 84 | 166 MB | 12,013 | 41M chars | ~10M |
  | All PDFs | 368 | 705 MB | 54,120 | 182M chars | ~45M |

  - Median page: about 3,350 characters (about 850 tokens). No filing averages less than 200 characters per page.
  - Text extraction of all 368 PDFs took about 5.5 minutes. Parse once and cache the result.
- **Index size estimates:**
  - Page text: about 180 MB.
  - Dense vectors, one per page, 1,024 dimensions, float32: 54,120 × 1,024 × 4 bytes ≈ 220 MB. About 1.1 GB if each page has about 5 sub-chunks.
  - BM25: do not build one global index. The router filters to the candidate filings first (A1), so build BM25 over the candidate pages at query time. One filing has at most 667 pages, so this is fast.
- **Consequences:**
  - No vector database. A brute-force numpy search over about 54,000 vectors takes milliseconds. A vector database is useful at millions of chunks.
  - Long-context baseline (Path A): about 120K tokens per question on average, about 18M input tokens for 150 questions. Path B multiplies this by the number of candidates.
  - Embedding all 45M tokens is the largest one-time cost. Embed only filings that can be candidates if this cost is too high.
- **Data gap:** 8 PDFs have no metadata entry: `ADOBE_2022Q2_10Q`, `AMCOR_2022_8K_2022-04-26`, `AMCOR_2022_8K_2022-07-01`, `BLOCK_2022_8K_dated-2022-01-28`, `BOSTONPROPERTIES_2015_10K`, `FOOTLOCKER_2022_10Q`, `ULTABEAUTY_2023Q1_EARNINGS`, `ULTABEAUTY_2023Q2_EARNINGS`. The two AMCOR files may be copies of filings that have metadata under a `dated-` name. The router needs metadata. **Decision (confirmed by the user, 2026-11-11):** parse company, period, and type from the file name, and remove a file if it is a copy of a filing that has metadata. Reason: if we leave files out, Path B becomes easier than it is in real use.
- **If false (millions of pages, or new filings each day):** use a vector database with metadata filters, a global sparse index, and incremental indexing (see A3).

## A8. Evidence is mostly in tables, and mostly on financial statement pages

- **Status:** Decided (measured 2026-11-11 on the 189 gold evidence items).
- **Measured:**
  - 130 of 189 items (69%) are table-heavy (25% or more of the tokens are numbers). Metrics-generated: 73 of 73. Domain-relevant: 37 of 62. Novel-generated: 20 of 54 (this type is mostly prose).
  - 105 of 189 evidence pages start with a financial statement title (balance sheet, income statement, cash flow statement). Metrics-generated: 66 of 73.
  - 57 of 150 questions name a statement ("balance sheet", "cash flow", "income statement").
- **Design consequences:**
  - Tables are the main case, not an edge case. The parser must keep each row label with its values and keep the year column headers.
  - At index time, tag each page with its statement type, found from the page title. A question that names a statement can then boost those pages. This is a cheap, deterministic signal.
  - The system must still handle prose, because novel-generated questions are mostly prose.
  - `question_type` is analysis metadata only. The system does not use it as input, because a real user does not give it.
- **If false (mostly prose evidence):** use smaller text chunks and dense retrieval. Table parsing matters less.

## A9. Evidence is a small, local part of the filing

- **Status:** Decided (measured 2026-11-11).
- **Measured:**
  - A question needs 1 to 3 pages of a filing with a median of 128 pages (about 1% to 2% of the filing).
  - The median evidence text is 1,271 characters. The median full page is 2,260 characters. So the evidence is about half a page.
  - 173 of 189 items are in the first 60% of the filing. Only 4 are in the last 20% (exhibits and signatures).
  - 35 questions have more than one evidence page. In 32 of them, the pages are 5 or fewer pages apart (the statements are next to each other). In 0 of them, the items are on the same page. In 2 of them, the pages are more than 20 pages apart.
- **Design consequences:**
  - Retrieval, not long context. The evidence is about 1% of the filing.
  - **One page is the retrieval unit.** It is about 2 times the size of the evidence, so it is not too large, and it matches the provenance requirement.
  - ~~Neighbor expansion~~ **Dropped by A13.** The statement pack already covers the adjacent statement pages. Expansion gave a small gain for 2.7 times more pages.
  - Multi-page questions still need a separate search for each value (query decomposition), for the few cases where the pages are far apart.
- **If false (evidence spread over the filing):** long context or an agent that reads many sections becomes the better choice.

## A10. PyMuPDF page index = gold page index

- **Status:** Decided (measured 2026-11-11).
- **Measured:** for 189 of 189 evidence items, the PyMuPDF text of page `evidence_page_num` matches `evidence_text_full_page`. No item matched better at an offset of ±1 or ±2.
- **Consequence:** the system can report provenance with the PyMuPDF page index. Report PDF page = index + 1.
- **If false (a different parser):** check the page alignment again before we trust any retrieval metric.

## A11. The 150 FinanceBench questions represent real user questions

- **Status:** Decided, with known limits (2026-11-11).
- **What the 150 questions are:** the public sample of the FinanceBench benchmark (10,231 questions in total). Each question has a gold answer, gold evidence (filing, page, text), and a justification, written by human annotators.
- **Three roles in this project:**
  1. **The task:** the deliverable lists an answer with provenance for each question.
  2. **The test set:** the labels are the only way to measure correctness. The system never sees `answer`, `evidence`, or `justification` at run time.
  3. **A proxy for real users:** there are no logs of real analyst questions, so these questions are the only sample of what users ask.
- **Known limits of the proxy:**
  - The benchmark authors chose the mix (50 questions of each type). Real use may differ.
  - All evidence for a question is in one filing. No question compares two companies or two filings.
  - Every question has an answer in its filing (see A2 for the eval fix).
- **Rule from now on:** tune prompts and thresholds on a dev split only. Do not look at the test split until the final run. We used the evidence labels of all 150 questions only for structural statistics (A8, A9, A10), which are true for any 10-K.
- **If false (users ask comparison questions, such as "Compare 3M's and Boeing's 2022 capex"):**
  - Add a **planning step** before the router. It splits the question into one sub-question per filing.
  - Route and answer each sub-question with the current pipeline.
  - Combine the sub-answers, with provenance from each filing.
  - The guardrails apply to each sub-answer. If one sub-answer is `NOT_FOUND`, the combined answer is `NOT_FOUND` or partial.

## A12. The PDF text layer is good enough to read tables

- **Status:** Decided for now (2026-11-11). Must be confirmed by an experiment.
- **Background:** a PDF has no tables. It stores characters at x,y positions. Each parser rebuilds rows and columns, and a bad rebuild silently attaches a number to the wrong row or year (the failure that A2 forbids).
- **Compared on two pages:**
  - Easy case: 3M FY2018 cash flow statement (`3M_2018_10K`, index 59). One header row of years.
  - Hard case: Best Buy International segment table (`BESTBUY_2024Q2_10Q`, index 17). Two header rows, prose and table on one page.

  | Method | Easy case | Hard case |
  |---|---|---|
  | PyMuPDF plain text | One cell per line. Years far from values. | Not checked in detail |
  | PyMuPDF `sort=True` (layout text) | Good. Rows on one line, columns under years. | Usable. Percent rows drift right relative to the date headers, so column alignment is approximate. |
  | PyMuPDF `find_tables` | Correct, but noise columns (`Col2`, `$` in its own column) | Not checked |
  | pdfplumber `extract_tables` | **Failed:** 21 fragments, because of the row shading | Not checked |
  | pdfplumber layout text | Good, like `sort=True` | Not checked |
  | Page image | Exact | Exact |

- **Problems that the hard case shows:**
  1. **Two header rows.** "July 29, 2023" appears twice, under "Three Months Ended" and under "Six Months Ended". Each value needs both headers.
  2. **Column headers are dates, not fiscal periods.** "July 29, 2023" is Q2 of **FY2024** for Best Buy. The question says "Q2 of FY2024". The system must map dates to the company's fiscal calendar. This is a key input to guardrail 6 (period check).
  3. **Units are in a caption** ("$ in millions") above the table, not in the cells.
  4. **"-" means zero.**
  5. **Prose and a table share one page**, so one page can hold more than one topic.
- **Decision: two representations for each page.**

  | Use | Representation | Why |
  |---|---|---|
  | Search (BM25, embeddings) and quote check | Plain text | Search needs only the words. The quote check needs a fixed text. |
  | Reading (LLM input for the answer) | Layout text (`sort=True`) | Keeps row and column alignment. Few tokens. |
  | Fallback | Page image, made only when needed | Image-only pages, approximate column alignment, period and unit check |

  - Do not use table detectors (`find_tables`, `extract_tables`). They fail in ways that we cannot predict.
  - Give the LLM the filing metadata (company, filing type, fiscal period) with the pages, so it can map column dates to fiscal periods.
- **Experiment to confirm:** for table questions in the dev split, give the LLM the gold page as layout text and as an image. Compare how often it extracts the correct value. If the image is clearly better, the image becomes the main reading format.
- **If false (the text layer is bad, or many pages are images):** use the page image as the main reading format, and OCR or a vision model for search text.

## A13. Retrieval: statement pack + BM25 is the baseline

- **Status:** Decided for now (2026-11-11). Measured on the dev split only (51 questions, 40 filings, 5,551 pages; `eval/split.json`, stratified by question type, seed 0). With 51 questions, differences under about 0.1 are noise.
- **Path A only** (search one filing). Query = the raw question. Metric = page recall@k (fraction of gold pages in the top k).
- **Measured:**

  | Method | r@1 | r@3 | r@5 | r@10 | Pages sent (k=5) |
  |---|---|---|---|---|---|
  | BM25 on the raw question | 0.16 | 0.24 | 0.27 | 0.31 | 5 |
  | BM25 + boost of the statement that the question names | 0.21 | 0.35 | 0.44 | 0.56 | 5 |
  | Statement pack only (all primary statement pages) | — | — | — | — | median 7 |
  | **Statement pack + BM25 top 5** | — | — | **0.78** | — | ~8.4 (v2 detector) |

  - BM25 by question type at k=5: metrics-generated 0.06, domain-relevant 0.18, novel-generated 0.59.
  - Statement pack by question type: metrics-generated 0.88, domain-relevant 0.59, novel-generated 0.12.
  - Statement pack + BM25 top 5 by question type: metrics-generated 0.88, domain-relevant 0.76, novel-generated 0.71.
  - Neighbor expansion (±1 page) on BM25 + boost at k=5: recall 0.44 → 0.50, but pages sent 5 → 13.
- **Why BM25 fails:** the gap between question and evidence is **conceptual**, not a synonym problem. The question names a concept ("quick ratio", "operating margin", "free cash flow conversion"). The evidence is a statement page that has only the inputs (current assets, inventory, revenue) and never the concept name. BM25 ranks the prose pages that discuss the concept (MD&A, notes) above the statement. Examples: 3M quick ratio, gold rank 80. AES return on assets, gold rank 133.
- **Statement pack: what it is.** The set of pages in one filing that hold the primary financial statements: income statement (or "statement of operations" / "of earnings"), comprehensive income, balance sheet (or "statement of financial position"), changes in equity, and cash flows. It is computed once per filing at index time and stored as a list of page indexes. At query time, these pages go to the LLM for every question on that filing, in addition to the search results.
- **Statement pack: how we detect it (v2, 2026-11-11).**
  - v1 searched the first 400 characters for a statement phrase. On `3M_2018_10K` it found 1 of the 5 real statement pages (indexes 55–59), and it added 7 notes pages that only mention "consolidated statements of income" in a sentence. Cause: the PDF text breaks words ("Incom e", "Shee t").
  - v2 rules: (1) remove all whitespace before matching, (2) the title must be a short line in the first 6 lines, (3) the page must be table-heavy (25% or more of the tokens contain a digit).
  - v2 on `3M_2018_10K`: exactly indexes 55–59. Dev split: median 4 pages per filing, maximum 8. Same recall as v1 (0.53 alone, 0.78 with BM25 top 5) with fewer pages: about 8.4 pages sent per question instead of about 12.7.
  - 5 dev filings have an empty pack (8-Ks and earnings releases have no standard statements, or the title format is different). Not checked one by one yet.
- **Decisions:**
  1. **Always send the statement pack** for a filing that has one. It costs about 4 pages (about 3K tokens) and covers most numeric questions. Every 10-K and 10-Q has primary statements, so this is a structural rule, not a fit to the questions.
  2. **Add BM25 top 5** for prose questions.
  3. **Drop neighbor expansion.** The statement pack already covers the adjacent statement pages. Expansion gave a small gain for 2.7 times more pages.
- **Open: the remaining 22% of gold pages.** Two candidates, both need a decision on tools:
  - Dense embeddings (a local model, or an API).
  - LLM query planning: the LLM converts the concept into the line items and sections it needs ("quick ratio" → cash, receivables, current liabilities; balance sheet), then searches for each one.
  - Hypothesis: query planning helps more than embeddings, because an embedding of "quick ratio" is also close to the liquidity prose. Test both on the dev split.
- **If false (filings without standard statements, such as 8-Ks or earnings releases):** the statement pack is empty, and retrieval depends on BM25 and the open candidates above.

## A14. Models: Qwen, served with vLLM on PACE ICE

- **Status:** Decided (user, 2026-11-11): Qwen3.5 on PACE ICE, one vision-language model for all calls. Sizes in A15.
- **Setup, copied from the user's existing ICE work** (the user's other ICE projects):
  - Login `$ICE_USER@login-ice.pace.gatech.edu` (set `ICE_USER` in `.env`), needs GlobalProtect VPN.
  - Everything under `~/scratch` (home is about 15 GB): venv, `HF_HOME`, pip cache, project.
  - GPU jobs: `-p ice-gpu --gres=gpu:h100:1` (also a100, l40s, h200).
  - `vllm serve` starts inside the Slurm job. The client calls it on `localhost` in the same job.
  - vLLM 0.27.1 in its own Python 3.12 venv (vLLM pins its own torch).
  - Code moves with `rsync`. Limit: 50 submitted jobs per user. Access is scheduled, not permanent.
- **Design consequences:**
  1. **Batch, not a live service.** One Slurm job = start vLLM, answer the questions, write results, stop.
  2. **Resumable.** Write each answer to a JSONL file when it finishes. On restart, skip finished questions.
  3. **OpenAI-compatible API.** The code uses the `openai` client with a `base_url`. A change of model or provider is a setting, not a code change.
  4. **Structured output from the decoder.** vLLM can force a JSON schema, so guardrail 2 (page + quote for each value) is enforced, not only requested.
  5. **Embeddings and reranking on the GPU.** Embedding about 54K pages on an H100 takes minutes. This removes the 8 GB M2 limit on the embedding choice. Qwen publishes embedding and reranker models, so one model family is possible.
  6. **Reproducibility.** Pin the vLLM version and the model revision. Use temperature 0 and a fixed seed. Write these next to each result.
- **Criteria for the model choice:**

  | Need | Constraint |
  |---|---|
  | Fit on one H100 (80 GB) | Dense up to about 32B in bf16, or larger with FP8 or mixture-of-experts |
  | Context | About 8 pages (7–8K tokens) + instructions. 16K is enough. |
  | Page-image fallback (A12) | A vision-language model |
  | Independent verifier (guardrail 7) | Ideally a different model from the answering model |

- **Decided: one vision-language model for all calls** (user, 2026-11-11).
- **Qwen models checked on Hugging Face (2026-11-11):**

  | Generation | Released | Sizes | Images |
  |---|---|---|---|
  | Qwen3 | Apr 2025 | 0.6B–32B | No (`Qwen3-8B` is text only) |
  | Qwen3-VL | Oct 2025 | 2B, 4B, 8B, 32B, 30B-A3B | Yes |
  | **Qwen3.5** | Feb 2026 | 0.8B, 2B, 4B, 9B, 27B, 35B-A3B, 122B-A10B, 397B-A17B | **Yes, all sizes** |
  | Qwen3.6 | Apr 2026 | 27B, 35B-A3B | Yes |
  | Qwen3.8 | Aug 2026 | 27B, Flash-Next, 2.4T-A95B | 27B: yes |

  - Qwen3.5 architecture: `Qwen3_5ForConditionalGeneration`. Revisions seen: `Qwen3.5-9B` @ `c202236235`, `Qwen3.5-27B` @ `fc05daec18`.
- **Check before the first run:** vLLM 0.27.1 (the splice pin) supports `Qwen3_5ForConditionalGeneration`. Test with a short smoke job on ICE.
- **Why images (summary of A12):** text extraction can attach a value to the wrong column. Use the page image only for (1) image-only pages, (2) unclear column alignment, (3) the period and unit check (guardrail 6). Search and the quote check use text.
- **If false (an API provider instead of ICE):** the batch and resumable design stays. Only `base_url` and the model name change. Rate limits and cost per token replace GPU hours.

## A15. Model size sweep

- **Status:** Decided (user, 2026-11-11).
- **Goal:** (1) find which model size is enough. User hypothesis: the largest model is best. Open to a surprise. (2) **Main question:** how much of the result comes from the LLM, and how much from the harness?
- **Ladder: Qwen3.5 2B, 9B, 27B** (all dense; user, 2026-11-11). Qwen3.5 is the only generation with a full size ladder, so size is the only variable.
  - Not used: 0.8B and 4B (user decision).
  - No dense Qwen3.5 model exists between 9B and 27B (checked 2026-11-11). 35B-A3B is mixture-of-experts with about 3B active, so it is not a point between them.
  - On a log scale the steps are 4.5× (2B → 9B) and 3× (9B → 27B), so the three points are almost evenly spaced.
  - Limit: with three points, the curve shows a trend, not its exact shape.
- **Second axis: harness level.** Each size runs in three settings:

  | Setting | Model gets | Measures |
  |---|---|---|
  | Bare | Retrieved pages + question. Free text. No guardrails, no code arithmetic. | The model alone |
  | Full harness | Same pages + structured output + code arithmetic + all guardrails | Model + harness |
  | Oracle | Gold pages + full harness | Ceiling without retrieval errors |

  - **Harness contribution = full harness − bare**, for each size. Plot it against model size.
  - If the gap shrinks with size: the harness replaces model ability, so a small model is enough. If the gap stays constant: the harness adds what size does not (correct arithmetic, checked quotes).
- **Expectation for 2B:** many guardrail checks fail, so coverage is low, but the wrong-answer rate may stay low. Schema enforcement (A14) guarantees valid JSON, so a failure is a failure of content, not of format.
- **Cost:** 3 sizes × 3 settings × 150 questions = 1,350 answer calls, plus calls to the fixed 27B verifier. A few H100 hours. One Slurm job per (size, setting) = 9 jobs, inside the 50-job limit.
- **Rules for a fair comparison:**
  1. One generation. Do not mix Qwen3-VL and Qwen3.5 in the size curve.
  2. Same retrieval, pages, prompts, decoding (temperature 0, fixed seed) for every size.
  3. Fixed verifier model (guardrail 7) for every size, for example Qwen3.5-27B. Only the answering model changes.
  4. Three settings for each size: bare, full harness, and oracle (see the table above).
- **Metrics for each size:** wrong-answer rate, coverage, selective accuracy (A2), and GPU-seconds per question.
- **Optional extra points:**
  - Qwen3.8-27B vs Qwen3.5-27B: same size, newer generation.
  - Qwen3.5-35B-A3B (MoE): 35B total, about 3B active per token. Total size vs active size.
- **Hypothesis to test:** with strict guardrails, small models have a similar wrong-answer rate to 27B but lower coverage, because the guardrails catch their errors and they abstain more.
- **GPU memory on one H100 (80 GB):** 27B bf16 ≈ 56 GB weights, enough room for a 16K context. 9B ≈ 19 GB.
- **If false (only smaller GPUs, such as L40S 48 GB):** run 27B in FP8 (`Qwen3.5-27B-FP8` exists), and say that the precision differs from the smaller models.

## A16. The LLM writes the formula, code does the arithmetic

- **Status:** Decided (user, 2026-11-11).
- **What the questions need (150 questions, question text only, keyword patterns, approximate):**
  - 80 name a computed metric (ratio, margin, growth, average). Only 17 of them give the formula, so in about 63 the model must know the definition.
  - 46 ask for rounding or units.
  - 43 ask for a judgment. 22 need a number first, then a judgment ("healthy liquidity based on its quick ratio").
  - About 20 say "if the metric is not relevant, explain why".
- **Options considered:**
  - A. The LLM does everything in one call. Simple, but arithmetic errors, and the math cannot be checked.
  - **B. The LLM extracts the values and writes a formula. Python computes. A second call writes the answer from the result.** Chosen.
  - C. A fixed formula library in code. Breaks on metrics outside the library. The benchmark also defines the same metric in different ways.
- **Why B:**
  - Arithmetic is always correct (supports A2).
  - The formula is part of the provenance: each value has a page and a quote, so a reader can check every step.
  - It fits the sweep (A15): "bare" = option A, "full harness" = option B. The difference measures what the harness adds.
- **Flow:**

  ```
  Call 1 (LLM): extract values + write formula      → JSON, schema enforced by vLLM
  Code:         quote check (guardrail 3), safe formula evaluation (guardrail 5)
  Call 2 (LLM): answer + judgment from the computed numbers and the quotes only
  ```

  - Extraction question: the formula is the value itself.
  - Judgment with no number: the values list is empty. Call 2 works from the quotes.
- **Formula: value names only, no numbers** (user, 2026-11-11). Allowed: value names, `+ - * /`, parentheses, and the functions `avg`, `sum`, `cagr`, `abs`.
  - Average of 3 years: `avg(a, b, c)`.
  - Percent: not in the formula. Call 1 sets `"display": "percent"`, and code formats the result.
  - CAGR: `cagr(first, last)`. Code computes the number of years from the `period` fields of the two values.
- **Call 1 output fields and why:**

  | Field | Why | Checked by |
  |---|---|---|
  | `raw` + `number` | Text as printed and its conversion. `(1,577)` must become −1577. | Code |
  | `scale` | Units are in the caption, not the cell (A12) | Guardrail 6 |
  | `period` + `column_header` | Which column was read and what fiscal period it means ("July 29, 2023" → "Q2 FY2024") | Guardrail 6 |
  | `page` + `quote` | Provenance | Guardrail 3. `raw` must also be in the quote. |
  | `formula` | Names only, so no number without a source | Guardrails 4, 5 |
  | `rounding`, `display` | Code formats the result exactly as the question asks | Code |
  | `status` | `found`, `not_applicable`, or `not_found` | Abstain logic |

  - **Text values (dates, names):** `number` can be empty. G3 still checks `raw` against the quote. The formula is the value name only. See R2 in `architecture.md`.

- **Call 2 input:** the checked quotes and computed numbers, plus the pages that the quotes come from. Not the other retrieved pages.
- **"Not applicable" is an answer, not an abstention.** Example: gross margin for a bank. The system must keep "the metric does not apply" (an `ANSWER` with evidence) separate from "I could not find the data" (`NOT_FOUND`).
- **Open experiment: a glossary of standard definitions in the prompt** (quick ratio, CAGR, FCF conversion). It can help the 2B model. Rule: the question's own definition always wins. Test on the dev split, with and without the glossary.
- **If false (the LLM must do the math itself, for example no code execution allowed):** guardrail 4 (number check) must recompute each number from the quoted values, so the code check moves from "compute" to "verify".

## A17. Provenance: code attaches it, the LLM never writes it

- **Status:** Decided (2026-11-11).
- **Requirement (from the task):** for each question, an answer and a provenance: page number plus the retrieved passage or table whenever possible, found automatically.
- **Rule:** call 2 writes only the answer text. The system attaches the provenance from call 1 values that passed guardrail 3 (the quote exists on the page). The LLM cannot cite a page that it did not read.
- **Judgment text:** call 2 cites quote IDs (`[v1, v3]`) for each claim, never free page numbers. Code converts each ID to its page and passage.
- **Final output, for each provenance item:**
  - `doc`: filing name.
  - `pdf_page`: page index + 1 (A10).
  - `quote`: the exact line that holds the value.
  - `passage`: the text block of the table or paragraph around the quote, from the layout text.
  - `column`, `scale`: the year column and the unit.
- **Page number has two meanings:** the PDF page and the number printed on the page can differ (Adobe: index 58 has "59" printed on it). We report the PDF page, because a reader can open the PDF there directly. The printed number can be an extra field.
- **Example (3M FY2018 capex):** `answer` "3M's FY2018 capital expenditure was $1,577 million.", `computation` "capex = purchases_of_ppe = 1,577", provenance `3M_2018_10K`, PDF page 60, quote "Purchases of property, plant and equipment (PP&E) (1,577)", column 2018, scale millions.
- **If false (the provenance must point to an exact cell or a bounding box):** store the x,y position of each text line at parse time, and return the box of the quote. PyMuPDF gives these positions.

## A18. Verification: order of checks, retries, and the verifier

- **Status:** Decided (user, 2026-11-11).
- **Principle:** cheap checks first. Code checks run before LLM checks and stop the pipeline early. The LLM verifier sees only answers that passed every code check.
- **Pipeline:**

  ```
  Call 1 (LLM)   G1 prompt rules, G2 JSON schema enforced by vLLM
  Code           G3 quote check, G5 formula check + safe evaluation
                 fail → retry call 1 once, with the error message
  Call 2 (LLM)   answer text, cites quote IDs
  Code           G4 number check
                 fail → retry call 2 once, with the error message
  Verifier       G6 + G7 in one call (fixed Qwen3.5-27B, with page images)
                 not a clear "yes" → abstain, no retry
  G8             conflict check (Path B, 2+ candidate filings)
  Output         ANSWER / NOT_FOUND / AMBIGUOUS + reason
  ```

- **Decisions:**
  1. **One retry, with the error message**, for code-check failures. No retry makes small errors fatal. Many retries let a wrong answer pass by luck, because the checks are not perfect.
  2. **Merge G6 and G7 into one verifier call.** It gets the question, the answer, the quotes, and the images of the cited pages. The image is the ground truth for column alignment (A12). Output:

     ```json
     {"period_ok": true, "unit_ok": true, "value_in_correct_column": true,
      "answer_supported": "yes | partly | no", "problem": "..."}
     ```

  3. **Abstain unless the verifier says a clear "yes"** and every flag is true. "Partly" counts as no (A2).
- **Check details from the data:**
  - G3 normalizes text: remove all whitespace, lowercase. The PDF text breaks words ("Incom e", A13). Compare against the layout text that the model saw, not the plain text.
  - G4 ignores numbers that are part of a period ("FY2018", "Q2").
- **To measure on the dev split:** how often the verifier rejects a correct answer (lost coverage) and accepts a wrong one (risk).
- **If false (a wrong answer is acceptable, A2 reversed):** keep G3–G5 as quality checks, drop the verifier, and always answer.

## A19. Retrieval gap experiment (planned, runs on ICE)

- **Status:** Designed (2026-11-11). Not run yet.
- **Models checked on Hugging Face (2026-11-11):** `Qwen3-Embedding-8B`, `Qwen3-Reranker-8B`, `Qwen3-VL-Embedding-2B/8B` (embeds page images), `Qwen3-VL-Reranker-2B/8B`.
- **Arms (Path A, dev split, page recall@k and "all gold pages found"):**

  | Arm | Retrieval | Tests |
  |---|---|---|
  | R0 | Statement pack + BM25 top 5 | Baseline (0.78) |
  | R1 | R0 + dense top 5 (`Qwen3-Embedding-8B` on page text), merged with BM25 | Do embeddings close the gap? |
  | R2 | R0 + LLM query planning (question → line items and sections → BM25 for each) | Does planning close the conceptual gap? |
  | R3 | R1 + R2 | Do they add up? |
  | R4 (optional) | R3 + `Qwen3-Reranker-8B` on the top 20 | Is a reranker worth one more model? |

- **Rules:**
  - Same page budget for every arm (for example 12 pages). Otherwise the arm that sends more pages wins for the wrong reason.
  - Planner model fixed at Qwen3.5-27B, like the verifier, so retrieval is the same for every size in the sweep (A15).
  - Choose the cheapest arm whose recall is within noise (about 0.1 on 51 questions) of the best.

## A20. Router for Path B: returns a candidate set, not one filing

- **Status:** Decided (2026-11-11). Measured with a rule-based router on the dev split (51 questions).
- **Universe:** 369 filings (361 with metadata + 8 parsed from the file name), 42 companies. Company key = the `doc_name` prefix, because the metadata company strings use a different format.
- **Rule-based router:** company = name or prefix string match. Period = years and quarters in the question (a filing of year N+1 also counts, because it reports year N). Type = "10-K", "10-Q", "8-K", "earnings" in the question. Rank: exact year, quarter filing only if the question names a quarter, then 10-K.
- **Measured:**

  | | Company found | Gold filing in candidates | Gold filing ranked first | Candidates (median) |
  |---|---|---|---|---|
  | Rule-based, end to end | 0.80 | 0.80 | 0.75 | 2 |
  | Correct company given | 1.00 | **1.00** | 0.86 | 3 |

  - Questions with no period: ranked-first accuracy 0.50 (4 questions).
- **Failure groups:**
  1. **Nicknames (8 of 51):** "AMEX", "JnJ", "JPM", "MGM". A string match cannot map them. Fix: an LLM call that must choose from the list of 42 companies (vLLM enforces the choice). The LLM knows common tickers and nicknames. The alias list is not built from the questions, so there is no overfitting.
  2. **No company in the question (2 of 51):** "Was there any drop in Cash & Cash equivalents between FY 2023 and Q2 of FY2024?" (Best Buy), and a board-vote question (Foot Locker). No router can solve these. Return `AMBIGUOUS` with the question "Which company?". Never guess.
  3. **Choice among one company's filings (14% wrong at rank 1):** dated 8-Ks (an event on May 26 is in the 8-K dated May 30), and questions with no period.
- **Decision:** the period and type filters never removed the gold filing (recall 1.00 when the company is correct). So the router returns a **candidate set** (median 3), not one filing. The 4-step flow in A1 then decides:
  - Run the per-filing pipeline on each candidate, up to 3, each with its own statement pack. Do not mix packs from different years in one prompt: the FY2023 10-K and the FY2022 10-K both have a FY2022 column, and a restated number can differ.
  - One candidate answers, the others return `NOT_FOUND` → `ANSWER` from that filing (case 3).
  - Candidates agree → `ANSWER`, cite the highest-ranked filing (case 2).
  - Candidates disagree → `AMBIGUOUS` with each value and its provenance (case 4).
- **Cost:** up to 3 times the calls of Path A for each question.
- **If false (users always name the company and the exact filing):** Path B reduces to Path A.

## A21. Pipeline runs in passes, one model per Slurm job

- **Status:** Decided (user, 2026-11-11).
- **Problem:** the verifier is always Qwen3.5-27B, but the answering model can be 2B or 9B. 9B (19 GB) + 27B (56 GB) on one 80 GB H100 leaves almost no memory for the context.
- **Design:** each Slurm job serves one model. Each pass writes JSONL, and the next pass reads it.

  | Pass | Model | Work |
  |---|---|---|
  | 0 | Qwen3.5-27B | Query planning for all questions (only if A19 selects it) |
  | 1 | Answering model (2B, 9B, or 27B) | Retrieval → call 1 → code checks → call 2 → G4. All retries happen here. |
  | 2 | Qwen3.5-27B | Verifier (G6 + G7) for every answer that passed pass 1, then G8 |
  | 3 | Judge (eval only) | Grades the final outputs against the gold answers |

- **Why it works:** every retry happens before the verifier (A18), so pass 2 never calls the answering model again. Pass 2 runs the same verifier on the outputs of all 3 sizes.
- **If false (two GPUs in one job, or one H200 with 141 GB):** both models can run in one job. The pass files stay useful as checkpoints.

## A22. Evaluation design

- **Status:** Decided (user, 2026-11-11).
- **Labels:** Correct / Incorrect / Refusal, the same three labels as the FinanceBench paper. Refusal = our `NOT_FOUND` or `AMBIGUOUS` status, not a judge decision. Metrics: wrong-answer rate, coverage, selective accuracy (A2).
- **Paper results as a reference:** `data/financebench/results/` has 16 configurations × 150 answers, each with a human label (2,400 labels). Example: GPT-4-Turbo singleStore = 75 correct, 17 incorrect, 58 refusals. singleStore ↔ our Path A, sharedStore ↔ Path B, oracle ↔ oracle. Use only to compare and to test the judge, never as system input.
- **Judge (two steps):**
  1. Numeric answers: code compares. Correct if our value matches at the precision of the gold answer, after units are made the same (millions vs billions). If no precision is given, 1% relative tolerance (user, 2026-11-11).
  2. Text and judgment answers: an LLM judge gets the question, the gold answer, the justification, and our answer. Output: JSON with a verdict and a one-line reason.
- **Judge model: `openai/gpt-oss-120b`** (user, 2026-11-11). 117B MoE, about 5B active, 4-bit, fits one H100. Apache 2.0, not gated. Different family from the verifier (Qwen), so their blind spots do not overlap. No newer gpt-oss exists (checked 2026-11-11). Gemma-4-31B-it was the other candidate. The user rejected it.
- **Judge vs verifier:** the verifier is part of the system and never sees the gold answer. The judge is part of the eval only and compares with the gold answer.
- **Eval components:**

  | # | Measures | How |
  |---|---|---|
  | E1 | Answer correctness | Labels above |
  | E2 | Judge | Code for numbers, gpt-oss-120b for text |
  | E3 | Trust in the judge | Run the judge on the paper's 2,400 labeled answers. Report agreement and the false-correct rate (judge says correct, humans say incorrect). |
  | E4 | Provenance | Exact page hit (cited page is a gold page). If not, check if the quote still supports the answer (the same number can be on 2 pages). |
  | E5 | Retrieval | Page recall@k by question type |
  | E6 | Abstention | 300 unanswerable questions built in code (below). False-answer rate on them. |
  | E7 | Path B | Routing accuracy, candidate recall, end-to-end labels. Manual check of "true ambiguity" cases. |
  | E8 | Statistics | Dev (51) for choices, test (99) once. Bootstrap 95% intervals. Paired tests between configurations. |
  | E9 | Cost | GPU-seconds and LLM calls per question |
  | E10 | No leakage | A test fails if pipeline code reads `answer`, `evidence`, or `justification`. Only eval code reads them. |

- **E6, unanswerable questions (correct output is always `NOT_FOUND`):**
  - Type (a), wrong filing: a real question + the filing of a company from a **different sector**, same period. Example: "3M FY2018 capex" + Boeing 2018 10-K. Dangerous output: Boeing's capex, presented as 3M's.
  - Type (b), year outside the filing: the year in the question moves **at least 5 years** before the filing year. Example: "3M FY2012 capex" + 3M 2018 10-K (which covers 2016–2018). Dangerous output: the 2016 value, presented as 2012.
  - One of each type per real question: 300 questions. The label is known from the construction, so no manual labeling.

## A23. Verifier and judge under a compute limit

- **Status:** Decided (user, 2026-11-11).
- **Problem:** the 27B verifier and the gpt-oss-120b judge need 80 GB GPUs. On ICE these were fully booked for hours. The free Blackwell GPUs expose 47.4 GB each.
- **Second problem:** the 27B verifier is the same family as the answering models, so their blind spots can overlap. A22 already chose a different family for the judge for this reason; the verifier did not follow the same rule.
- **Decision:** a vision model from a **different family** that fits in 47 GB verifies the 2B and 9B runs: `microsoft/Phi-4-reasoning-vision-15B` (Jan 2026, MIT, 15B; supported by vLLM 0.32 as `Phi4ForCausalLMV`). The judge for these runs is `openai/gpt-oss-20b`, calibrated on the same 2,400 human labels as gpt-oss-120b (E3).
- **Candidates checked (2026-11-11):** Phi-4-reasoning-vision-15B (chosen: newest, reasons step by step), Ministral-3-14B-Instruct-2512, granite-vision-4.1-4b, Kimi-VL-A3B-Instruct. Gemma excluded (user). InternVL and MiniCPM-V excluded (Qwen-based language models).
- **Measurement:** Phi-4 also verifies the dev-1 candidates that gpt-oss-120b already graded, so Phi-4 and 27B are compared on the same answers.
- **27B, the 27B verifier and gpt-oss-120b** stay queued and run when an 80 GB GPU frees up.
- **Reasoning verifier:** no enforced JSON schema (it would cut off the reasoning). The model reasons, then ends with one JSON object, which the client reads.
- **Limitation for the write-up:** the compute limit decided the verifier and judge sizes, not the dev results.
- **Future scope (more compute):** 27B or larger answering model; a large verifier from another family; gpt-oss-120b as the judge for every run; verifier thinking on; several samples per question with agreement voting; retrieval arm R3 with a larger page budget.

## A7. Acceptable wrong-answer rate

- **Status:** Decided (2026-11-11). There is no hard target. Keep the wrong-answer rate as low as possible, and report the full trade-off curve.
- **Note:** the unanswerable test questions in A2 belong to the eval design. We design the evals separately, later.
- **Question:** How many wrong answers are acceptable, and at what cost in coverage? Example: "under 2% wrong, even if coverage falls to 70%".
- **If a fixed target:** tune the guardrail thresholds to meet it on the dev split.
- **If no target:** report the full trade-off curve and let the reader choose the operating point.

## A3. The corpus is static

- **Status:** Decided (2026-11-11). True for this task: the dataset is pinned to one commit.
- **Assumption:** The 84 question documents do not change, and no new filings arrive.
- **If false:** Index new filings incrementally. Add parser regression tests, because filing formats change over time.

## A4. Page-level provenance is enough

- **Status:** Decided (2026-11-11). Page + quote + passage, see A17.
- **Assumption:** A page number + the retrieved passage or table is enough provenance. The task asks for "the page number and, whenever possible, the retrieved passage or table".
- **If false (the user needs the exact cell or sentence):** Chunk below the page level, and keep the page ID on each chunk. Return the exact quote and check it against the page text.

## A5. Latency and cost are not hard limits

- **Status:** Decided (2026-11-11). Offline batch runs on ICE (A14). Report GPU-seconds per question (A15), but do not optimize for latency.
- **Assumption:** This is an offline evaluation of 150 questions. There is no per-question latency limit.
- **If false (an interactive product with a budget):** Use a fixed pipeline instead of an agent loop. Send fewer pages. Use a smaller model for routing and reranking.
