"""
`metis chat` — conversational shell over one matter (Phase 1, text-only).

The soul of Metis-for-Peter: ask anything about YOUR matter — where things
stand, what's outstanding, what a document says, draft a request letter.

Every model output passes through rails.enforce() (advice-shape gate) before
it reaches the user. The matter folder is read-only; anything Metis drafts is
printed/saved under METIS_HOME with the DRAFT watermark.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from . import DEFAULT_MATTER, METIS_HOME
from . import llm, rails
from .inventory import scan
from .state_machine import MatterState

MAX_DOC_CHARS = 6000
CONTEXT_DOCS = ("STATUS.md", "REDLINE-DPO-2026-05-27.md", "drafts/00_FILL_IN_CHECKLIST.md")


def _matter_context(matter: Path) -> str:
    st = MatterState(matter)
    results = scan(matter)
    inv_lines = [
        f"- {r.item.name}: {r.state.upper()}"
        + (f" (evidence: {', '.join(r.evidence[:2])})" if r.evidence else "")
        for r in results
    ]
    doc_parts = []
    for rel in CONTEXT_DOCS:
        p = matter / rel
        if p.exists():
            doc_parts.append(f"### {rel}\n{p.read_text(errors='ignore')[:MAX_DOC_CHARS]}")
    drafts = sorted((matter / "drafts").glob("*.md")) if (matter / "drafts").is_dir() else []
    return (
        f"MATTER: {matter.name} · workflow {st.summary()}\n\n"
        f"DOCUMENT INVENTORY (T1 template):\n" + "\n".join(inv_lines) + "\n\n"
        f"DRAFTS ON FILE: {', '.join(d.name for d in drafts)}\n\n"
        + "\n\n".join(doc_parts)
    )


def repl(matter: Path | None = None) -> int:
    matter = (matter or DEFAULT_MATTER).resolve()
    if not matter.is_dir():
        print(f"matter folder not found: {matter}", file=sys.stderr)
        return 1
    provider = llm.provider_name()
    if provider == "none":
        print("No LLM provider configured — `metis chat` needs one.", file=sys.stderr)
        print("Set ANTHROPIC_API_KEY / GEMINI_API_KEY, or keep app/.env Forge creds.", file=sys.stderr)
        return 1

    print(f"╭─ Metis · {matter.name} · provider: {provider}")
    print(f"│  {rails.DISCLAIMER}")
    print("│  Commands: /save (save last answer as DRAFT file) · /quit")
    print("╰─")

    system = rails.SYSTEM_PROMPT + "\n\nMATTER CONTEXT:\n" + _matter_context(matter)
    history: list[dict] = []
    last_answer = ""

    while True:
        try:
            user = input("\nyou › ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not user:
            continue
        if user in ("/quit", "/q", "exit"):
            return 0
        if user == "/save":
            if not last_answer:
                print("nothing to save yet")
                continue
            out = METIS_HOME / f"METIS-DRAFT-{date.today().isoformat()}.md"
            out.write_text(rails.watermark(last_answer))
            print(f"saved → {out}")
            continue

        history.append({"role": "user", "content": user})
        try:
            raw = llm.complete(system, history[-12:])
        except Exception as e:
            print(f"⚠️  provider error: {e}", file=sys.stderr)
            history.pop()
            continue
        gated = rails.enforce(raw)
        last_answer = gated
        history.append({"role": "assistant", "content": gated})
        print(f"\nmetis › {gated}")


if __name__ == "__main__":
    sys.exit(repl(Path(sys.argv[1]) if len(sys.argv) > 1 else None))
