"""
Provider-pluggable LLM client (stdlib-only, no deps).

Provider resolution order:
  1. ANTHROPIC_API_KEY (env)          → Anthropic Messages API
  2. GEMINI_API_KEY (env or app/.env) → Gemini OpenAI-compatible endpoint
  3. Forge gateway (app/.env)         → OpenAI-compatible chat completions
  4. none                             → raises ProviderUnavailable

The app's .env (metis/app/.env) is read for the Forge/Gemini credentials so
the CLI shares the app's working keys without duplicating secrets.
"""

from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path

from . import METIS_HOME

APP_ENV = METIS_HOME / "app/.env"


class ProviderUnavailable(RuntimeError):
    pass


def _read_app_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if APP_ENV.exists():
        for line in APP_ENV.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def _post_json(url: str, headers: dict, payload: dict, timeout: int = 120) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def complete(system: str, messages: list[dict], max_tokens: int = 2000) -> str:
    """messages: [{"role": "user"|"assistant", "content": str}, ...] → assistant text."""
    app_env = _read_app_env()

    anthropic_key = os.environ.get("ANTHROPIC_API_KEY") or app_env.get("ANTHROPIC_API_KEY")
    if anthropic_key:
        data = _post_json(
            "https://api.anthropic.com/v1/messages",
            {"x-api-key": anthropic_key, "anthropic-version": "2023-06-01"},
            {
                "model": os.environ.get("METIS_ANTHROPIC_MODEL")
                or app_env.get("DRAFTING_MODEL", "claude-sonnet-5"),
                "system": system,
                "messages": messages,
                "max_tokens": max_tokens,
            },
        )
        return "".join(b.get("text", "") for b in data.get("content", []))

    gemini_key = os.environ.get("GEMINI_API_KEY") or app_env.get("GEMINI_API_KEY")
    forge_url = app_env.get("BUILT_IN_FORGE_API_URL")
    forge_key = app_env.get("BUILT_IN_FORGE_API_KEY")

    # OpenAI-compatible payload shared by Gemini-compat + Forge
    oai_messages = [{"role": "system", "content": system}] + messages

    if gemini_key:
        try:
            data = _post_json(
                "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
                {"Authorization": f"Bearer {gemini_key}"},
                {"model": app_env.get("LLM_MODEL", "gemini-2.5-flash"),
                 "messages": oai_messages, "max_tokens": max_tokens},
            )
            return data["choices"][0]["message"]["content"]
        except Exception:
            pass  # fall through to Forge (Gemini key was 403 as of May)

    if forge_url and forge_key:
        data = _post_json(
            f"{forge_url.rstrip('/')}/v1/chat/completions",
            {"Authorization": f"Bearer {forge_key}"},
            {"model": app_env.get("LLM_MODEL", "gemini-2.5-flash"),
             "messages": oai_messages, "max_tokens": max_tokens},
        )
        return data["choices"][0]["message"]["content"]

    raise ProviderUnavailable(
        "No LLM provider available. Set ANTHROPIC_API_KEY or GEMINI_API_KEY, "
        f"or ensure Forge credentials exist in {APP_ENV}."
    )


def provider_name() -> str:
    app_env = _read_app_env()
    if os.environ.get("ANTHROPIC_API_KEY") or app_env.get("ANTHROPIC_API_KEY"):
        return "anthropic"
    if os.environ.get("GEMINI_API_KEY") or app_env.get("GEMINI_API_KEY"):
        return "gemini(+forge fallback)" if app_env.get("BUILT_IN_FORGE_API_KEY") else "gemini"
    if app_env.get("BUILT_IN_FORGE_API_KEY"):
        return "forge"
    return "none"
