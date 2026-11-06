# Task: Financial Document QA (FinanceBench)

Status: setup is complete. Implementation has not started.

## Goal

Build a QA system that answers each FinanceBench question from the provided financial documents.
The approach is open: PDF parsing, chunking, indexing, retrieval, LLM, and prompts are my choice.
I can implement my own ideas or reproduce a reference paper. Any API or tool is allowed.

Benchmark: https://github.com/patronus-ai/financebench

## Required output for each question

- An answer.
- Provenance: where the answer came from in the document, found automatically by the system.
  Give the page number and, whenever possible, the retrieved passage or table.

## Deliverable

A short document (1-2 pages) that covers:

- System design at a high level: parsing, retrieval, generation.
- My answers to each question, with provenance.
- What worked, what did not work, and what I would change with more time.

Code (GitHub link or zip) is encouraged but not required.

## Dataset facts (checked 2026-11-06)

Location: `data/financebench/` (git-ignored). Run `scripts/fetch_data.sh` to download it.
Commit: `cc39aeb4afdf33909ee1412188bf89035950c2eb`.

- `data/financebench_open_source.jsonl`: 150 questions, 84 documents, 32 companies.
- Question types: 50 metrics-generated, 50 domain-relevant, 50 novel-generated.
- `pdfs/`: 368 PDFs. `data/financebench_document_information.jsonl` lists 361 documents.
- The 84 question documents all exist and open. They have 12,013 pages in total (min 4, median 130, max 549).
- Each document has a mean of at least 200 text characters per page. Individual pages can still be images only.
- 35 questions have more than one evidence item. All evidence is in the document of the question.

## Things to remember

- Evidence page numbers are zero-indexed. Convert them before I report PDF page numbers.
- Evidence items use the key `doc_name`. The README says `evidence_doc_name`, which is incorrect.
- Do not let the system see `answer`, `justification`, or `evidence`. Use these fields for evaluation only.
- `results/` holds answers from other models. Do not use it as input.
- `vectorstores/` holds only a README. There is no prebuilt index.

## Open decisions

- LLM provider and model. No API key is set yet. Copy `.env.example` to `.env` and add a key.
- Scope of retrieval: use `doc_name` to search one document, or search all documents.
- Embedding model. It is not installed yet because it depends on the design.

## Environment

- Python 3.11 in `.venv` (the system Python 3.14 is not used).
- Install: `.venv/bin/pip install -r requirements.txt`.
