# Architecture

Final design of the FinanceBench QA system (design review, 2026-11-11).
Each decision links to its entry in [`assumptions.md`](assumptions.md), which holds the evidence.

## Goal and priority

- Answer each question about a financial filing, with provenance: PDF page, quote, and passage or table.
- **Top priority: no wrong answers (A2).** When the system is unsure, it says `NOT_FOUND` or `AMBIGUOUS`, with a reason.

## 0. Requirements check (task text, checked 2026-11-11)

| Requirement | Covered by | Status |
|---|---|---|
| Use the provided documents | Path A: given filing. Path B: all 369 filings. | OK |
| Free choice of parsing, chunking, retrieval, LLM, prompts | A12, A13, A14, A16 | OK |
| An answer for each question | Every question gets an output row, always (R1 below) | Fixed by R1 |
| Provenance: page number + passage or table | `pdf_page`, `quote`, `passage` (A17) | OK |
| Evidence found automatically | Code builds provenance from retrieved pages. Gold evidence is never an input (A11). | OK |
| Facts include revenue, ratios, **dates** | Text values allowed (R2 below) | Fixed by R2 |
| Deliverable: 1–2 pages | Short document that links to the GitHub README (R3 below) | Fixed by R3 |
| Deliverable: answers to each question with provenance | GitHub README with all 150 rows (R3) | Fixed by R3 |
| Deliverable: what worked, what did not, what to change | Experiment log + reversed decisions (A13 detector v1, neighbor expansion, BM25 alone) | OK |
| Code (optional) | Git repo. Data is git-ignored. No AI attribution in commits. | OK |

**R1. No checked citation → no answer** (user, firm, 2026-11-11). The system abstains rather than give an answer that has no checked provenance. Every question still gets a row. For `NOT_FOUND` and `AMBIGUOUS`, the row shows the status, which check failed and why (for example "verifier: value is in the 2017 column, not 2018"), and the pages searched. The row never shows the draft value that failed the checks. In metrics, an abstention counts as not correct.

**R2. Text values** (confirmed by the user, 2026-11-11). In call 1, `number` can be empty for a text value (a date, a segment name). The quote check (G3) still applies to `raw`. The formula is the value name only. An `ANSWER` must have at least one provenance item.

**R3. Deliverable format** (user, 2026-11-11).
- The short document links to the GitHub README. The README holds the full analysis and all 150 answers with status and provenance.
- The page limit does not constrain the architecture. Trim the write-up later.
- **One main configuration** gives the official answers. Choose it on the dev split (for example "Qwen3.5-27B, full harness, Path A"). The README can show every configuration.

**R4. Reference point.** The FinanceBench paper's results (`data/financebench/results/`) map to our setups: singleStore ↔ Path A, sharedStore ↔ Path B, oracle ↔ oracle. Use them to compare results only, never as input.

**R5. Priorities.**

| Priority | Scope | Why |
|---|---|---|
| P0 | Path A, one model, full harness, 150 answers with provenance, 2-page document + appendix | Meets every requirement |
| P1 | Size sweep (A15), retrieval experiment (A19), verifier error rates (A18) | Defends the approach |
| P2 | Path B evaluation, layout text vs images (A12), glossary (A16), optional sweep points | Extra depth |

## 1. Offline: indexing (once, on the Mac or an ICE CPU node)

```
369 PDFs (361 with metadata + 8 parsed from the file name)          A6, A20
  │
  ├─ PyMuPDF, for each page:
  │     plain text         → search + quote check                     A12
  │     layout text        → LLM reading input (sort=True)            A12
  │     page index         → provenance (PDF page = index + 1)        A10
  │
  ├─ Statement pack, for each filing:                                 A13
  │     pages whose title is a primary statement
  │     (whitespace removed, short title line in the first 6 lines, table-heavy page)
  │
  ├─ Filing metadata: company key, period, type, fiscal calendar     A20, A12
  │
  └─ (if A19 selects it) dense vectors per page, Qwen3-Embedding-8B   A19
```

- No vector database. About 54K pages fit in memory (A6).
- BM25 is built at query time over the candidate filing. One filing has at most 667 pages (A6).
- Page images are rendered only when needed (A12).

## 2. Online: one question (Slurm batch job on ICE, vLLM on one H100)

```
question (+ optional doc_name)                                         A1
  │
  ▼
ROUTER                                                                 A20
  doc_name given → [that filing]                                       Path A
  else → LLM picks company from the 42-company list (enforced choice)
       → period + type filters → up to 3 candidate filings             Path B
  no company in the question → AMBIGUOUS "Which company?"
  │
  ▼  for each candidate filing, separately (never mix filings in one prompt)
RETRIEVAL                                                              A13, A19
  statement pack + BM25 top 5   (+ the arm that A19 selects)
  │
  ▼
CALL 1: extract (answering model)                                      A16
  input:  pages as layout text + filing metadata + question
  output: JSON, schema enforced by vLLM                                G1, G2
          status, values [raw, number, scale, period, column_header, page, quote], formula
  │
  ▼
CODE CHECKS                                                            A18
  G3 quote exists on page (normalized); raw value inside quote
  G5 formula = names + avg/sum/cagr/abs only; safe evaluation
  fail → retry call 1 once with the error message, then NOT_FOUND
  │
  ▼
CALL 2: answer (answering model)                                       A16, A17
  input:  checked quotes + computed result + the pages they come from
  output: answer text, each claim cites quote IDs [v1, v2]
  │
  ▼
CODE CHECK                                                             A18
  G4 each number in the answer = a checked value or the computed result
  fail → retry call 2 once, then NOT_FOUND
  │
  ▼
VERIFIER (Gemma 4 12B, other family, with page images)                A18, A23
  G6 + G7: period_ok, unit_ok, value_in_correct_column, answer_supported
  anything except a clear "yes" → NOT_FOUND
  │
  ▼  (Path B, 2+ candidates)
CONFLICT CHECK (G8)                                                    A1, A20
  one answers, others NOT_FOUND → ANSWER from that filing
  all agree                     → ANSWER, cite the highest-ranked filing
  disagree                      → AMBIGUOUS, each value with provenance
  │
  ▼
OUTPUT: ANSWER | NOT_FOUND | AMBIGUOUS
  answer, computation, provenance [doc, pdf_page, quote, passage, column, scale]   A17
  provenance is built by code from checked values, never written by the LLM
```

## 3. Experiments

| ID | Question | Arms | Where |
|---|---|---|---|
| A19 | What closes the last 22% of retrieval recall? | R0 baseline, R1 embeddings, R2 query planning, R3 both, R4 reranker | ICE |
| A12 | Is layout text enough to read tables, or are images better? | Gold page as layout text vs as image | ICE |
| A16 | Does a glossary of definitions help? | With vs without | ICE |
| A18 | How often is the verifier wrong? | False rejects (lost coverage), false accepts (risk) | ICE |
| A15 | How much comes from the model, how much from the harness? | Qwen3.5 2B / 9B / 27B × bare / full harness / oracle | ICE |

Rules: decide on the dev split only (51 questions, `eval/split.json`). Run the test split (99 questions) once, at the end (A11). Eval design is separate.

## 4. If an assumption changes

Blast radius: **Low** = one setting or one function. **Medium** = one stage changes. **High** = more than one stage, or the output contract changes.

| # | Assumption | If false | What changes | Blast radius |
|---|---|---|---|---|
| A2 | A wrong answer is worse than none | The system must always answer | Drop the verifier and `NOT_FOUND`. G3–G5 stay as quality checks. Metrics: accuracy only. | **High** (output contract) |
| A11 | Each question needs one filing | Comparison questions ("3M vs Boeing capex") | New planning stage before the router: split, route each part, combine. Guardrails per part. | **High** (new stage + new combine step) |
| A8, A9 | Evidence is in tables, small, local | Evidence is prose, spread over the filing | Statement pack loses value. Smaller chunks, dense retrieval, or long context / an agent that reads sections. | **High** (retrieval redesign) |
| A1 | Path B: the user may not name the filing | Users always name it | Router reduces to Path A. Nothing else changes. | Low |
| A20 | Candidate set, up to 3 | Many candidates (no period, large company) | Cost grows ×N. Add page-level ranking across filings, or ask the user. | Medium (router) |
| A13 | Filings have standard statements | 8-Ks, earnings releases, foreign formats | Empty statement pack. Retrieval depends on BM25 + the A19 arm. | Medium (retrieval) |
| A12 | The text layer reads tables well | Bad text layer, scanned pages | Page image becomes the main reading input. OCR or vision embeddings for search. | Medium (parsing + reading) |
| A6 | About 54K pages, static (A3) | Millions of pages, new filings daily | Vector database with metadata filters, global sparse index, incremental indexing, parser regression tests. | Medium (indexing only) |
| A5 | No latency limit | Interactive product | Fewer pages, smaller router and planner model, verifier only on high-risk answers, parallel candidates. | Medium |
| A16 | Code may run the arithmetic | No code execution | G4 recomputes each number from quoted values ("verify" instead of "compute"). | Low |
| A17, A4 | Page + quote + passage is enough | Exact cell or bounding box needed | Store x,y positions at parse time and return the quote's box. | Low |
| A18 | Strict verifier, abstain unless "yes" | Coverage matters more | Accept "partly", or skip the verifier for pure extraction questions. | Low (threshold) |
| A14 | Qwen on ICE | An API provider | Change `base_url` and the model name. Batch + resumable design stays. | Low |
| A15 | 2B / 9B / 27B ladder | Other sizes or generations | Experiment config only. | Low |
| A10 | PyMuPDF page index = gold index | Another parser | Check page alignment again before trusting any metric. | Low |

**Observation for the report:** most assumption changes touch one stage, because each stage has one job and a fixed interface (candidates → pages → values → checked answer). Only three changes cut across stages: the output contract (A2), the question shape (A11), and the evidence shape (A8, A9). These are the assumptions to watch.
