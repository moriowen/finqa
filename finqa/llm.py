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
STREAM = os.environ.get("FINQA_STREAM") == "1"


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
    if STREAM:  # benchmark mode: stream to measure time to first token; same request otherwise
        return await _chat_stream(cl, messages, schema, max_tokens, model, extra, kw, t0)
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


async def _chat_stream(cl, messages, schema, max_tokens, model, extra, kw, t0) -> dict:
    stream = await cl.chat.completions.create(model=model or MODEL, messages=messages, temperature=0, max_tokens=max_tokens,
                                              extra_body=extra, stream=True, stream_options={"include_usage": True}, **kw)
    parts, ttft, finish, usage = [], None, None, None
    async for ch in stream:
        if ch.usage:
            usage = ch.usage.model_dump()
        for c in ch.choices:
            d = c.delta
            if ttft is None and (getattr(d, "content", None) or getattr(d, "reasoning_content", None)):
                ttft = round(time.time() - t0, 3)
            if getattr(d, "content", None):
                parts.append(d.content)
            if c.finish_reason:
                finish = c.finish_reason
    text = "".join(parts)
    out = {"text": text, "usage": usage, "seconds": round(time.time() - t0, 2), "finish": finish, "ttft": ttft}
    if schema is not None:
        try:
            out["json"] = parse_json(text)
        except Exception as e:  # noqa: BLE001
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
