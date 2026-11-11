import pytest

from finqa.checks import number_check, numbers_in_text, quote_on_page, raw_in_quote
from finqa.formula import FormulaError, evaluate, parse_raw, present


@pytest.mark.parametrize("raw,val", [("(1,577)", -1577), ("$ 5,363", 5363), ("24.2 %", 24.2),
                                     ("(8.8)%", -8.8), ("-", 0.0), ("1.73", 1.73), ("Corporate", None),
                                     ("−473", -473)])
def test_parse_raw(raw, val):
    assert parse_raw(raw) == val


def test_formula_basic_and_functions():
    v = {"cash": 10.0, "rec": 5.0, "cl": 10.0}
    assert evaluate("(cash + rec) / cl", v, {}) == 1.5
    assert evaluate("avg(cash, rec)", v, {}) == 7.5
    assert evaluate("-cash", v, {}) == -10


def test_formula_cagr_uses_periods():
    r = evaluate("cagr(a, b)", {"a": 100.0, "b": 121.0}, {"a": "FY2020", "b": "FY2022"})
    assert abs(r - 0.1) < 1e-9


@pytest.mark.parametrize("f", ["cash * 100", "__import__('os')", "cash ** rec", "round(cash, rec)",
                               "cash.real", "unknown + cash", "[cash]"])
def test_formula_rejects(f):
    with pytest.raises(FormulaError):
        evaluate(f, {"cash": 1.0, "rec": 2.0}, {})


def test_present():
    assert present(1577e6, "number", "millions", 0) == (1577.0, "1,577 million")
    assert present(0.0435, "percent", "units", 1) == (4.3, "4.3%")


def test_quote_check_ignores_pdf_spacing():
    page = "Consolidated Statement of Incom e\nPurchases of property, plant and equipment (PP&E)   (1,577)  (1,373)"
    assert quote_on_page("Purchases of property, plant and equipment (PP&E) (1,577)", [page])
    assert quote_on_page("Consolidated Statement of Income", [page])
    assert not quote_on_page("Purchases of property (1,999)", [page])
    assert quote_on_page("Purchases of property ... (1,577)", [page])


def test_raw_in_quote():
    assert raw_in_quote("(1,577)", "Purchases of PP&E (1,577) (1,373)")
    assert raw_in_quote("$ 5,363", "Net income $5,363")
    assert not raw_in_quote("1,578", "Purchases of PP&E (1,577)")


def test_numbers_skip_periods():
    nums = [n[0] for n in numbers_in_text("In FY2018 and Q2 2023 the 10-K shows $1,577 million [v1, v2] in 2018.")]
    assert nums == [1577.0]


def test_number_check():
    vals = [{"raw": "(1,577)", "scale": "millions"}]
    assert number_check("3M's FY2018 capex was $1,577 million [v1].", vals, -1577e6, 1577.0) == []
    assert number_check("Capex was $1.58 billion.", vals, -1577e6, 1577.0) == []
    assert number_check("Capex was $1,700 million.", vals, -1577e6, 1577.0) == ["$1,700"]
    assert number_check("It has two segments.", [], None, None) == []


def test_constants_only_from_question():
    from finqa.formula import question_constants
    c = question_constants("DPO = 365 * average payables / COGS for FY2022")
    assert c == {365.0}
    assert evaluate("365 * cash / rec", {"cash": 1.0, "rec": 2.0}, {}, c) == 182.5
    with pytest.raises(FormulaError):
        evaluate("100 * cash", {"cash": 1.0}, {}, c)
    assert evaluate("max(cash, rec)", {"cash": 1.0, "rec": 2.0}, {}) == 2.0


def test_quote_label_plus_one_column():
    page = "Total net revenue                 9,497,578           4,713,500           3,298,177"
    assert quote_on_page("Total net revenue | 4,713,500", [page])
    assert not quote_on_page("Total net revenue | 4,713,501", [page])


def test_number_check_skips_dates():
    assert number_check("As of December 31, 2022 the ratio was 1.2 [v1].", [{"raw": "1.2", "scale": "units"}], 1.2, 1.2) == []
