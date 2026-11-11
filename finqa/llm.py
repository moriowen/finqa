"""Thin client for a vLLM server with the OpenAI-compatible API (A14).

One Slurm job serves one model (A21). The server URL comes from FINQA_BASE_URL.
"""
from __future__ import annotations
import asyncio
import base64
import json
import os
import re
import time

from openai import AsyncOpenAI, BadRequestError

BASE_URL = os.environ.get("FINQA_BASE_URL", "http://localhost:8000/v1")
MODEL = os.environ.get("FINQA_MODEL", "")
SEED = 0


class LLMError(RuntimeError):
    pass


def client() -> AsyncOpenAI:
    return AsyncOpenAI(base_url=BASE_URL, api_key="none", timeout=900, max_retries=2)


def image_part(png: bytes) -> dict:
    return {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(png).decode()}}


def strip_think(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text or "", flags=re.S).strip()


def parse_json(text: str) -> dict:
    t = strip_think(text)
    m = re.search(r"\{.*\}", t, re.S)
    if not m:
        raise LLMError(f"no JSON object in output: {t[:200]!r}")
    return json.loads(m.group(0))


async def chat(cl: AsyncOpenAI, messages: list[dict], *, schema: dict | None = None, max_tokens: int = 2048,
               thinking: bool = False, model: str | None = None, reasoning_effort: str | None = None) -> dict:
    """One request. Returns {'text', 'json' (if schema), 'usage', 'seconds'}."""
    extra = {"seed": SEED}
    if reasoning_effort is None:
        extra["chat_template_kwargs"] = {"enable_thinking": thinking}
    kw = {}
    if schema is not None:
        kw["response_format"] = {"type": "json_schema", "json_schema": {"name": "out", "schema": schema, "strict": True}}
    if reasoning_effort is not None:
        kw["reasoning_effort"] = reasoning_effort
    t0 = time.time()
    try:
        r = await cl.chat.completions.create(model=model or MODEL, messages=messages, temperature=0,
                                             max_tokens=max_tokens, extra_body=extra, **kw)
    except BadRequestError:
        if schema is None:
            raise
        # fallback: a decoder that rejects length limits in the schema gets the schema without them
        kw["response_format"]["json_schema"]["schema"] = _strip_limits(schema)
        r = await cl.chat.completions.create(model=model or MODEL, messages=messages, temperature=0,
                                             max_tokens=max_tokens, extra_body=extra, **kw)
    text = r.choices[0].message.content or ""
    out = {"text": text, "usage": r.usage.model_dump() if r.usage else None, "seconds": round(time.time() - t0, 2),
           "finish": r.choices[0].finish_reason}
    if schema is not None:
        try:
            out["json"] = parse_json(text)
        except Exception as e:  # noqa: BLE001 - truncated or malformed output is a content failure
            out["json"] = None
            out["error"] = f"bad JSON: {e}"
    return out


def _strip_limits(schema):
    if isinstance(schema, dict):
        return {k: _strip_limits(v) for k, v in schema.items() if k not in ("maxItems", "maxLength", "minItems")}
    if isinstance(schema, list):
        return [_strip_limits(x) for x in schema]
    return schema


async def gather_limited(coros, limit: int = 16):
    sem = asyncio.Semaphore(limit)

    async def run(c):
        async with sem:
            return await c
    return await asyncio.gather(*(run(c) for c in coros))
