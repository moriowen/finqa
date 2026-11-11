"""File locations. Everything is relative to the repo root, so the same code runs on the Mac and on ICE."""
from pathlib import Path
import os

ROOT = Path(os.environ.get("FINQA_ROOT", Path(__file__).resolve().parents[1]))
DATA = ROOT / "data" / "financebench"
PDFS = DATA / "pdfs"
QUESTIONS = DATA / "data" / "financebench_open_source.jsonl"
DOC_INFO = DATA / "data" / "financebench_document_information.jsonl"
PAPER_RESULTS = DATA / "results"

ARTIFACTS = ROOT / "artifacts"          # git-ignored caches (parsed pages, vectors)
PAGES = ARTIFACTS / "pages"             # one JSON per filing
RUNS = ROOT / "runs"                    # pass outputs (JSONL), committed
SPLIT = ROOT / "eval" / "split.json"

for p in (ARTIFACTS, PAGES, RUNS):
    p.mkdir(parents=True, exist_ok=True)
