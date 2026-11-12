### Model size × harness (150 questions, Path A; verifier Gemma 4 12B, judge gpt-oss-20b)

| Model | Setting | Correct | Wrong | Refused | Wrong-answer rate [95% CI] | Coverage | Selective accuracy | Page hit | Test only (99): wrong / correct |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-27B (FP8) | bare | 101 | 48 | 1 | 32% [25 to 39] | 99% | 68% | n/a | 31% / 68% |
| Qwen3.5-27B (FP8) | full | 80 | 20 | 50 | 13% [8 to 19] | 67% | 80% | 85% | 10% / 55% |
| Qwen3.5-27B (FP8) | oracle | 92 | 13 | 45 | 9% [5 to 13] | 70% | 88% | 100% | 7% / 60% |
| Qwen3.5-9B | bare | 93 | 57 | 0 | 38% [30 to 45] | 100% | 62% | n/a | 36% / 64% |
| Qwen3.5-9B | full | 72 | 16 | 62 | 11% [6 to 16] | 59% | 82% | 84% | 11% / 46% |
| Qwen3.5-9B | full-gloss | 62 | 16 | 72 | 11% [6 to 16] | 52% | 79% | 86% | 12% / 40% |
| Qwen3.5-9B | oracle | 73 | 17 | 60 | 11% [7 to 17] | 60% | 81% | 100% | 11% / 51% |
| Qwen3.5-2B | bare | 77 | 72 | 1 | 48% [39 to 56] | 99% | 52% | n/a | 44% / 55% |
| Qwen3.5-2B | full | 12 | 2 | 136 | 1% [0 to 3] | 9% | 86% | 79% | 1% / 7% |
| Qwen3.5-2B | full-gloss | 12 | 0 | 138 | 0% [0 to 0] | 8% | 100% | 83% | 0% / 8% |
| Qwen3.5-2B | oracle | 15 | 4 | 131 | 3% [1 to 5] | 13% | 79% | 100% | 3% / 9% |

### Questions with no answer in the filing (E6, 290 per model)

| Model | Setting | False answers | Wrong filing | Shifted year |
|---|---|---|---|---|
| Qwen3.5-27B (FP8) | bare | 22/290 (8%) | 7% | 9% |
| Qwen3.5-27B (FP8) | full | 1/290 (0%) | 0% | 1% |
| Qwen3.5-9B | bare | 20/290 (7%) | 5% | 9% |
| Qwen3.5-9B | full | 0/290 (0%) | 0% | 0% |
| Qwen3.5-9B | full-gloss | 0/290 (0%) | 0% | 0% |
| Qwen3.5-2B | bare | 53/290 (18%) | 17% | 20% |
| Qwen3.5-2B | full | 0/290 (0%) | 0% | 0% |
| Qwen3.5-2B | full-gloss | 0/290 (0%) | 0% | 0% |

### Path B: no filing given (27B, full harness)

| Correct | Wrong | Refused | Wrong-answer rate | Coverage |
|---|---|---|---|---|
| 76 | 16 | 58 | 11% | 61% |

### FinanceBench paper baselines (human labels, same 150 questions)

| Paper configuration | Correct | Wrong | Refused | Wrong-answer rate | Coverage |
|---|---|---|---|---|---|
| gpt-4-1106-preview_oracle | 128 | 22 | 0 | 15% | 100% |
| gpt-4-1106-preview_sharedStore | 29 | 20 | 101 | 13% | 33% |
| gpt-4-1106-preview_singleStore | 75 | 17 | 58 | 11% | 61% |
| gpt-4_oracle | 126 | 15 | 9 | 10% | 94% |
| gpt-4_sharedStore | 25 | 13 | 112 | 9% | 25% |
| gpt-4_singleStore | 63 | 16 | 71 | 11% | 53% |
| llama2_sharedStore | 29 | 104 | 17 | 69% | 89% |
| llama2_singleStore | 62 | 81 | 7 | 54% | 95% |

### Verifier (Gemma 4 12B) vs judge, on answers that passed the code checks

| Run | Checked | Accepted correct | Accepted wrong (leaks) | Rejected correct (lost) | Rejected wrong (caught) |
|---|---|---|---|---|---|
| all-9b-full | 97 | 70 | 18 | 2 | 7 |
| all-27b-full | 106 | 82 | 19 | 1 | 4 |
| all-2b-full | 18 | 12 | 2 | 1 | 3 |
| pathb-27b-full | 165 | 127 | 27 | 1 | 10 |
| all-27b-oracle | 119 | 92 | 15 | 5 | 7 |
| all-9b-full-gloss | 85 | 62 | 16 | 1 | 6 |
| all-9b-oracle | 96 | 74 | 16 | 2 | 4 |
| all-2b-full-gloss | 14 | 12 | 0 | 1 | 1 |
| all-2b-oracle | 24 | 15 | 4 | 1 | 4 |
| devv1-27b-full-r0 | 25 | 21 | 2 | 0 | 2 |
| devv1-9b-full-r0 | 38 | 25 | 2 | 3 | 8 |
| devv1-2b-full-r0 | 9 | 5 | 1 | 1 | 2 |
| dev-9b-full-r0 | 38 | 28 | 3 | 2 | 5 |
| dev-2b-full-r0 | 10 | 5 | 1 | 1 | 3 |

### Judge calibration (E3): gpt-oss-20b (used) vs the paper's 2,400 human labels

Agreement 77%. Judge says *correct* when humans say *incorrect*: 6%. Judge says *incorrect* when humans say *correct*: 13%.

| Human \ Judge | correct | incorrect | refusal |
|---|---|---|---|
| correct | 987 | 145 | 3 |
| incorrect | 31 | 485 | 12 |
| refusal | 26 | 339 | 372 |

### Judge calibration (E3): gpt-oss-120b (reference) vs the paper's 2,400 human labels

Agreement 80%. Judge says *correct* when humans say *incorrect*: 6%. Judge says *incorrect* when humans say *correct*: 11%.

| Human \ Judge | correct | incorrect | refusal |
|---|---|---|---|
| correct | 1004 | 130 | 1 |
| incorrect | 31 | 494 | 3 |
| refusal | 24 | 281 | 432 |

### Cost per question (pass 1 only)

| Run | LLM calls | LLM seconds | Tokens |
|---|---|---|---|
| all-9b-full | 2.2 | 58.7 | 17,561 |
| all-27b-full | 2.3 | 189.5 | 19,907 |
| all-2b-full | 2.0 | 21.3 | 21,845 |
| all-27b-bare | 1.0 | 69.6 | 11,031 |
| all-27b-oracle | 2.5 | 58.2 | 5,968 |
| all-9b-bare | 1.0 | 30.7 | 11,014 |
| all-9b-full-gloss | 2.2 | 59.8 | 18,242 |
| all-9b-oracle | 2.2 | 25.4 | 4,932 |
| all-2b-bare | 1.0 | 7.3 | 11,019 |
| all-2b-full-gloss | 2.0 | 24.2 | 22,875 |
| all-2b-oracle | 2.2 | 14.0 | 6,203 |

### Where answers are lost (all-9b-full, 150 questions)

| Stage outcome | Questions |
|---|---|
| answered (all checks passed) | 88 |
| extractor: evidence not in the pages | 18 |
| number check (G4) failed twice | 12 |
| formula check (G5) failed twice | 12 |
| quote check (G3) failed twice | 11 |
| verifier rejected | 9 |
