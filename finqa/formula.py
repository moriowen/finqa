"""Safe formula evaluation (A16, guardrail G5).

A formula may contain only value names, + - * /, parentheses, unary minus, and the functions
avg, sum, cagr, abs. No numeric constants: every number must come from a quoted value.
"""
from __future__ import annotations
import ast
import math
import re

SCALES = {"units": 1.0, "thousands": 1e3, "millions": 1e6, "billions": 1e9}
FUNCS = {"avg", "sum", "cagr", "abs"}


class FormulaError(ValueError):
    pass


def parse_raw(raw: str) -> float | None:
    """'(1,577)' -> -1577.0, '$ 5,363' -> 5363.0, '24.2 %' -> 24.2, '-' -> 0.0, 'Corporate' -> None."""
    s = raw.strip().replace("—", "-").replace("–", "-").replace("−", "-")
    if s in {"-", "--", "—"}:
        return 0.0
    neg = s.startswith("(") and s.rstrip("%").rstrip().endswith(")")
    core = re.sub(r"[\s$€£,%()]", "", s)
    if core.startswith("-"):
        neg, core = True, core[1:]
    if not re.fullmatch(r"\d+(\.\d+)?|\.\d+", core):
        return None
    v = float(core)
    return -v if neg else v


def _year(period: str | None) -> float | None:
    """'FY2018' -> 2018, 'Q2 FY2024' -> 2024.5, '2022' -> 2022."""
    if not period:
        return None
    m = re.search(r"(19|20)\d{2}", period)
    if not m:
        m2 = re.search(r"FY\s?(\d{2})\b", period, re.I)
        if not m2:
            return None
        y = 2000 + int(m2.group(1))
    else:
        y = int(m.group(0))
    q = re.search(r"Q([1-4])", period, re.I)
    return y + (int(q.group(1)) - 1) / 4 if q else float(y)


def check_formula(formula: str, names: set[str]) -> ast.Expression:
    try:
        tree = ast.parse(formula.strip(), mode="eval")
    except SyntaxError as e:
        raise FormulaError(f"formula is not valid: {e.msg}")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.Load, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)):
            continue
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            continue
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            continue
        if isinstance(node, ast.Call):
            if not (isinstance(node.func, ast.Name) and node.func.id in FUNCS) or node.keywords:
                raise FormulaError("only avg, sum, cagr, abs are allowed as functions")
            continue
        if isinstance(node, ast.Name):
            if node.id in FUNCS:
                continue
            if node.id not in names:
                raise FormulaError(f"unknown value name '{node.id}' (names: {sorted(names)})")
            continue
        if isinstance(node, ast.Constant):
            raise FormulaError(f"numeric constant {node.value!r} is not allowed: use only value names")
        raise FormulaError(f"'{type(node).__name__}' is not allowed in a formula")
    return tree


def evaluate(formula: str, values: dict[str, float], periods: dict[str, str | None]) -> float:
    tree = check_formula(formula, set(values))

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Name):
            return values[n.id]
        if isinstance(n, ast.UnaryOp):
            v = ev(n.operand)
            return -v if isinstance(n.op, ast.USub) else v
        if isinstance(n, ast.BinOp):
            a, b = ev(n.left), ev(n.right)
            if isinstance(n.op, ast.Add):
                return a + b
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                return a * b
            if b == 0:
                raise FormulaError("division by zero")
            return a / b
        if isinstance(n, ast.Call):
            f = n.func.id
            args = [ev(a) for a in n.args]
            if not args:
                raise FormulaError(f"{f} needs arguments")
            if f == "avg":
                return sum(args) / len(args)
            if f == "sum":
                return sum(args)
            if f == "abs":
                if len(args) != 1:
                    raise FormulaError("abs takes one argument")
                return abs(args[0])
            if f == "cagr":
                if len(n.args) != 2 or not all(isinstance(a, ast.Name) for a in n.args):
                    raise FormulaError("cagr takes two value names: cagr(first, last)")
                y0, y1 = _year(periods.get(n.args[0].id)), _year(periods.get(n.args[1].id))
                if y0 is None or y1 is None or y1 <= y0:
                    raise FormulaError("cagr needs two values whose periods give an increasing year")
                first, last = args
                if first <= 0 or last <= 0:
                    raise FormulaError("cagr needs positive values")
                return (last / first) ** (1 / (y1 - y0)) - 1
        raise FormulaError("unsupported formula")

    r = ev(tree)
    if not math.isfinite(r):
        raise FormulaError("result is not finite")
    return r


def present(result: float, display: str, out_scale: str, rounding: int | None) -> tuple[float, str]:
    """Convert an absolute result to what the question asked for. Returns (number, text)."""
    if display == "percent":
        v = result * 100
        suffix = "%"
    else:
        v = result / SCALES.get(out_scale, 1.0)
        suffix = {"thousands": " thousand", "millions": " million", "billions": " billion"}.get(out_scale, "")
    if rounding is not None:
        v = round(v, rounding)
        txt = f"{v:,.{rounding}f}"
    else:
        txt = f"{v:,.4f}".rstrip("0").rstrip(".")
    return v, txt + suffix
