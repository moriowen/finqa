"""Prompts and output schemas (A16, A17, A18)."""
from __future__ import annotations

SCALE_ENUM = ["units", "thousands", "millions", "billions"]

GLOSSARY = """Standard definitions (use them only when the question does not define the metric; the question's own definition always wins):
- Gross margin = gross profit / revenue. Operating margin = operating income / revenue.
- Quick ratio = (cash and equivalents + short-term investments + receivables) / current liabilities.
- Current (working capital) ratio = total current assets / total current liabilities.
- Free cash flow = cash from operations - capital expenditure. FCF conversion = free cash flow / net income.
- Capital expenditure = purchases of property, plant and equipment.
- Fixed asset turnover = revenue / average net PP&E. Inventory turnover = cost of goods sold / average inventory.
- Days payable outstanding = 365 * average accounts payable / (cost of goods sold + change in inventory).
- Return on assets = net income / average total assets. CAGR = cagr(first, last).
- Effective tax rate = income tax expense / income before taxes. Dividend payout ratio = dividends / net income."""

CALL1_SYSTEM = """You are a careful financial analyst. You answer questions about one SEC filing, using ONLY the pages given below.

Your task in this step: find the evidence, and write a formula. Do not compute anything yourself.

Rules:
1. Use only the given pages. Do not use your own knowledge of the company's numbers.
2. Give only the values that the answer needs, at most 12. For every value you use, copy the "quote" EXACTLY from the page: the row label and the number as printed, from one line of the page. Do not shorten numbers, do not change signs, do not reformat.
3. "raw" is the value exactly as printed in that line, for example "(1,577)" or "$5,363" or "24.2%". For a non-numeric fact (a name, a date, a segment), raw is that text.
4. "scale" is the unit of the table, usually stated in a caption such as "(In millions)". Use "units" for per-share data, percentages, counts and text.
5. "period" is the fiscal period of the column you read, for example "FY2018" or "Q2 FY2024". "column_header" is the header text of that column as printed, for example "2018" or "July 29, 2023". Companies whose fiscal year does not end in December label columns with dates: map them to the fiscal period with the filing information given.
6. "name" is a short identifier: lowercase letters, digits and underscores, for example capex_2018.
7. "formula" uses ONLY the "name" identifiers of your values (exactly as written in the name fields, never row labels), + - * /, parentheses, and the functions avg(...), sum(...), abs(x), max(...), min(...), cagr(first, last). Never write a number in the formula, except a constant that the question itself states (for example 365 if the question defines a days-based metric with 365). For an average of two years use avg(a, b). For a question that asks for one value, the formula is that value's name. For a text answer, leave the formula empty.
8. "display": "percent" ONLY if the question asks for a percentage, a margin or a growth rate (write the formula as a fraction; the system multiplies by 100). Use "number" for amounts and for ratios such as a quick ratio, a current ratio or a turnover (these are not percentages). Use "text" for non-numeric answers.
9. "out_scale": the unit the question asks for (for example "USD millions" -> millions). Use "units" for ratios and per-share values.
10. "rounding": the number of decimal places that the question asks for, or -1 if it does not say.
11. "status":
   - "found": the pages contain the evidence.
   - "not_applicable": the question asks about a metric that is not meaningful for this company (for example gross margin for a bank). Give the values that show why.
   - "not_found": the pages do not contain the evidence for THIS company and THIS period. If the filing belongs to a different company, or does not cover the asked period, answer not_found. Never use a value from another period or another company as a substitute.
12. For a judgment question (for example "is the liquidity healthy?"), extract the numbers needed for the metric, and write the formula for the metric."""

CALL1_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["found", "not_applicable", "not_found"]},
        "values": {"type": "array", "maxItems": 12, "items": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "maxLength": 64},
                "raw": {"type": "string", "maxLength": 200},
                "scale": {"type": "string", "enum": SCALE_ENUM},
                "period": {"type": "string"},
                "column_header": {"type": "string"},
                "page": {"type": "integer"},
                "quote": {"type": "string", "maxLength": 400},
            },
            "required": ["name", "raw", "scale", "period", "column_header", "page", "quote"],
            "additionalProperties": False}},
        "formula": {"type": "string"},
        "display": {"type": "string", "enum": ["number", "percent", "text"]},
        "out_scale": {"type": "string", "enum": SCALE_ENUM},
        "rounding": {"type": "integer"},
        "reason": {"type": "string"},
    },
    "required": ["status", "values", "formula", "display", "out_scale", "rounding", "reason"],
    "additionalProperties": False,
}

CALL2_SYSTEM = """You write the final answer to a financial question. You get ONLY checked evidence: values with IDs and exact quotes, and the result that the system computed from them.

Rules:
1. Use only the given evidence and the computed result. Do not add numbers that are not in the evidence or the result.
2. State the computed result exactly as given. Do not recompute it and do not round it differently.
3. After each claim, cite the IDs of the values that support it, in square brackets, for example [v1, v3]. Write plain text only, no JSON.
4. If the question asks for a judgment (for example "is it healthy?"), give a clear yes or no, then the reason, based only on the evidence.
5. If the status is not_applicable, say that the metric is not meaningful for this company and why, with citations.
6. Answer in 1 to 4 sentences. Start with the direct answer (the number with its unit, or yes/no, or the name), then give a short reason from the evidence. Never answer with only one word."""

CALL2_SCHEMA = {
    "type": "object",
    "properties": {"answer": {"type": "string"}, "citations": {"type": "array", "items": {"type": "string"}}},
    "required": ["answer", "citations"],
    "additionalProperties": False,
}

BARE_SYSTEM = """You are a financial analyst. Answer the question about the SEC filing, using the pages below. Give the final answer in 1 to 4 sentences, and say which page it comes from."""

VERIFIER_SYSTEM = """You check an answer to a financial question before it is shown to a user. A wrong answer is much worse than no answer.

You get the question, the filing information, the evidence values (each with the page, the quote, the column and the period that the extractor reported), the computation, the final answer, and IMAGES of the cited pages. The images are the ground truth.

Important:
- "page N" means the N-th page of the PDF file. It is NOT the page number printed on the page. Ignore printed page numbers completely; never reject because of them.
- Code already checked that every quote exists, character by character, in the text of its page. A quote may contain only the row label and the one value that was used. Do not reject a quote for leaving out other columns.
- Your job is to check what code cannot: that each value is in the column of the right period, the right scale, that the formula is a correct definition of what the question asks, and that the answer follows from the evidence.

Check:
- period_ok: each value comes from the period that the question asks for (map column dates to fiscal periods with the filing information). True if not relevant.
- unit_ok: the scale of each value matches the table caption, and the answer states the unit that the question asks for. True if not relevant.
- value_in_correct_column: in the IMAGE, each quoted number is in the row and the column that the extractor reported. True if not relevant.
- answer_supported: "yes" only if the evidence fully supports the final answer and the answer actually answers the question asked; "partly" if some part is not supported or the question is only partly answered; "no" otherwise. Also answer "no" if the filing is about a different company than the question, or if the formula is not a correct definition for what the question asks.
- problem: one sentence that describes the problem, or "" if there is none."""

VERIFIER_SCHEMA = {
    "type": "object",
    "properties": {
        "period_ok": {"type": "boolean"},
        "unit_ok": {"type": "boolean"},
        "value_in_correct_column": {"type": "boolean"},
        "answer_supported": {"type": "string", "enum": ["yes", "partly", "no"]},
        "problem": {"type": "string"},
    },
    "required": ["period_ok", "unit_ok", "value_in_correct_column", "answer_supported", "problem"],
    "additionalProperties": False,
}

PLAN_SYSTEM = """You plan the search in a financial filing. For the question, list short search queries that name the line items or the topics that the evidence page contains, using the words that a 10-K or 10-Q uses (for example "quick ratio" -> "cash and cash equivalents", "accounts receivable", "total current liabilities"). Also list which primary statements are needed: bs (balance sheet), is (income statement), cf (cash flow statement), eq (equity), ci (comprehensive income). Give 2 to 6 queries."""

PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "queries": {"type": "array", "items": {"type": "string"}},
        "statements": {"type": "array", "items": {"type": "string", "enum": ["bs", "is", "cf", "eq", "ci"]}},
    },
    "required": ["queries", "statements"],
    "additionalProperties": False,
}

ROUTER_SYSTEM = """Identify the company that the question is about. Choose exactly one key from the list, or "NONE" if the question does not name or clearly identify a company. Common tickers and nicknames count (for example JPM = JPMorgan, JnJ = Johnson & Johnson, AMEX = American Express). Also extract the fiscal years, the quarter and the document type if the question states them."""


def router_schema(keys: list[str]) -> dict:
    return {
        "type": "object",
        "properties": {
            "company": {"type": "string", "enum": keys + ["NONE"]},
            "years": {"type": "array", "items": {"type": "integer"}},
            "quarter": {"type": "string", "enum": ["Q1", "Q2", "Q3", "Q4", "none"]},
            "doc_type": {"type": "string", "enum": ["10K", "10Q", "8K", "EARNINGS", "none"]},
            "date": {"type": "string"},
        },
        "required": ["company", "years", "quarter", "doc_type", "date"],
        "additionalProperties": False,
    }
