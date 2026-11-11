"""Smoke test for a served model: text, enforced JSON schema, and an image (A14).

Run inside a job after `vllm serve`:  python -m finqa.smoke
"""
import asyncio
import json
import sys

from . import llm, parse


async def main() -> int:
    cl = llm.client()
    ok = True
    r = await llm.chat(cl, [{"role": "user", "content": "What is 17 multiplied by 23? Answer with the number only."}],
                       max_tokens=50)
    print("TEXT:", repr(r["text"]), r["seconds"], "s")
    ok &= "391" in r["text"] and "<think>" not in r["text"]

    schema = {"type": "object", "properties": {"value": {"type": "string"}, "page": {"type": "integer"}},
              "required": ["value", "page"], "additionalProperties": False}
    r = await llm.chat(cl, [{"role": "user", "content": "Page 12 says: revenue was $4,210 million. Return the value and the page."}],
                       schema=schema, max_tokens=100)
    print("JSON:", repr(r["text"]), r.get("json"))
    ok &= isinstance(r.get("json"), dict) and set(r["json"]) == {"value", "page"}

    png = parse.render_png("3M_2018_10K", 59)
    r = await llm.chat(cl, [{"role": "user", "content": [
        llm.image_part(png),
        {"type": "text", "text": "Read the value of 'Purchases of property, plant and equipment (PP&E)' in the 2018 column. "
                                 "Answer with the value as printed."}]}], max_tokens=50)
    print("IMAGE:", repr(r["text"]), r["seconds"], "s")
    ok &= "1,577" in r["text"]
    print("SMOKE", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
