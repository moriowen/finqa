"""Plumbing tests with a fake LLM, plus the leakage guard (E10)."""
import asyncio
import json
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from finqa import answer, corpus, retrieve, verify

PKG = Path(__file__).resolve().parents[1] / "finqa"
needs_data = pytest.mark.skipif(not (PKG.parent / "artifacts" / "pages" / "3M_2018_10K.json.gz").exists(),
                                reason="parsed pages not available")


def test_pipeline_never_reads_gold():
    """E10: only finqa/evals and the CLI's oracle mode may read gold fields."""
    for f in PKG.glob("*.py"):
        src = f.read_text()
        if f.name == "cli.py":
            src = re.sub(r"if a\.mode == \"oracle\":\n\s+from \.evals\.gold import oracle_pages.*\n", "", src)
            src = src.replace("from .evals.unanswerable import build", "")
        assert "evals.gold" not in src and "evals import gold" not in src, f.name
        for field in ('["answer"]', '["evidence"]', '["justification"]', "'answer'", "'evidence'"):
            if f.name in ("corpus.py",):
                assert field not in src, (f.name, field)


def test_corpus_questions_have_no_gold_fields():
    q = corpus.questions()[0]
    assert set(vars(q)) == {"id", "question", "doc_name"}


class FakeLLM:
    """Returns call-1 JSON, then call-2 JSON."""
    def __init__(self, outs):
        self.outs = list(outs)
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    async def _create(self, **kw):
        text = json.dumps(self.outs.pop(0))
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text), finish_reason="stop")],
                               usage=None)


@needs_data
def test_full_pipeline_with_fake_llm():
    q = corpus.Question(id="t1", question="What is the FY2018 capital expenditure amount (in USD millions) for 3M?",
                        doc_name="3M_2018_10K")
    sel = retrieve.select_pages("3M_2018_10K", q.question)
    assert 59 in sel["pages"]  # the cash flow statement is in the statement pack
    call1 = {"status": "found", "values": [{"name": "capex_2018", "raw": "(1,577)", "scale": "millions", "period": "FY2018",
             "column_header": "2018", "page": 60,
             "quote": "Purchases of property, plant and equipment (PP&E) (1,577)"}],
             "formula": "abs(capex_2018)", "display": "number", "out_scale": "millions", "rounding": 0, "reason": ""}
    call2 = {"answer": "3M's FY2018 capital expenditure was $1,577 million [v1].", "citations": ["v1"]}
    rec = asyncio.run(answer.run_full(FakeLLM([call1, call2]), q, "3M_2018_10K", sel["pages"], sel["ranked"]))
    assert rec["status"] == "CANDIDATE", rec
    assert rec["shown_text"] == "1,577 million"
    assert rec["provenance"][0]["pdf_page"] == 60
    assert "1,577" in rec["provenance"][0]["passage"]


@needs_data
def test_bad_quote_is_retried_then_not_found():
    q = corpus.Question(id="t2", question="FY2018 capex for 3M?", doc_name="3M_2018_10K")
    sel = retrieve.select_pages("3M_2018_10K", q.question)
    bad = {"status": "found", "values": [{"name": "capex", "raw": "(1,999)", "scale": "millions", "period": "FY2018",
           "column_header": "2018", "page": 60, "quote": "Purchases of property (1,999)"}],
           "formula": "capex", "display": "number", "out_scale": "millions", "rounding": 0, "reason": ""}
    rec = asyncio.run(answer.run_full(FakeLLM([bad, bad]), q, "3M_2018_10K", sel["pages"], sel["ranked"]))
    assert rec["status"] == "NOT_FOUND" and "twice" in rec["reason"]
    assert "1,999" not in json.dumps({k: v for k, v in rec.items() if k != "attempts"})  # no failed value in the row


def test_combine_g8():
    base = {"question": "q", "pages_shown": [1]}
    a = {**base, "qid": "x", "doc": "A", "status": "ANSWER", "answer": "Yes, 1.2 [v1]", "shown": 1.2, "formula": "f",
         "shown_text": "1.2", "values": [], "provenance": [{"pdf_page": 1}]}
    b = {**a, "doc": "B", "shown": 1.5}
    nf = {**base, "qid": "x", "doc": "C", "status": "NOT_FOUND", "reason": "r"}
    assert verify.combine("x", "q", [a, nf], ["A", "C"])["status"] == "ANSWER"
    assert verify.combine("x", "q", [a, b], ["A", "B"])["status"] == "AMBIGUOUS"
    assert verify.combine("x", "q", [nf], ["C"])["status"] == "NOT_FOUND"
    assert verify.combine("x", "q", [], [])["status"] == "AMBIGUOUS"
