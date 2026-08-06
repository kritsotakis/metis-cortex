"""
Adversarial critique re-runner (M5) — Stage 10 of the workflow spec.

An independent pass (separate system prompt from chat) reads the assembled
matter material and writes the case FOR THE OPPOSING PARTY: counter-arguments,
weaknesses, compliance landmines, credibility risks — REDLINE-style F-numbered
findings. Framed as "things to discuss with your solicitor", never directives.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from . import DEFAULT_MATTER, METIS_HOME
from . import llm, rails
from .state_machine import MatterState, Stage

CRITIQUE_SYSTEM = f"""You are an independent adversarial reviewer for a self-represented
party's OWN Australian family-law matter pack. Your job: read the material and write the
strongest case the OPPOSING party / a sceptical Registrar could make against it.

Output format — markdown:
- Start with a 3-line overall exposure summary.
- Then findings numbered F1, F2, ... each with: **severity** (🔴 critical / 🟠 high / 🟡 medium),
  the weakness, the specific document/paragraph it lives in, and what evidence or fix would
  close it (as a documentation task, NOT legal advice).
- End with: "{rails.LAWYER_FLAG}"

Rules: you critique DOCUMENTATION (gaps, inconsistencies, unsupported assertions,
missing exhibits, tone risks). You never predict outcomes, never recommend strategy,
never say what the party "should" do — every fix is framed as "documentation to obtain/
amend, to discuss with your solicitor."
"""

MAX_CHARS_PER_DOC = 12000
DEFAULT_TARGETS = ("drafts",)


def gather(matter: Path, targets: tuple[str, ...] = DEFAULT_TARGETS) -> str:
    parts: list[str] = []
    for t in targets:
        base = matter / t
        files = sorted(base.glob("*.md")) if base.is_dir() else ([base] if base.exists() else [])
        for f in files:
            parts.append(f"\n\n===== {f.relative_to(matter)} =====\n"
                         + f.read_text(errors="ignore")[:MAX_CHARS_PER_DOC])
    return "".join(parts)


def run(matter: Path | None = None) -> Path:
    matter = (matter or DEFAULT_MATTER).resolve()
    material = gather(matter)
    if not material.strip():
        raise SystemExit(f"no draft material found under {matter}/drafts")
    print(f"➜ critique pass over {matter.name} drafts ({len(material)//1000}k chars) …")
    raw = llm.complete(
        CRITIQUE_SYSTEM,
        [{"role": "user", "content": "Run the adversarial critique over this material:\n" + material}],
        max_tokens=4000,
    )
    gated = rails.enforce(raw)
    out = METIS_HOME / f"CRITIQUE-{matter.name.upper()}-{date.today().isoformat()}.md"
    out.write_text(rails.watermark(
        f"# Adversarial critique — {matter.name} ({date.today().isoformat()})\n\n{gated}"
    ))
    st = MatterState(matter)
    if st.stage in (Stage.INVENTORY, Stage.RETRIEVE, Stage.PROCESS):
        st.advance(Stage.CRITIQUE, f"critique run → {out.name}")
    print(f"✅ critique → {out}")
    return out


if __name__ == "__main__":
    run(Path(sys.argv[1]) if len(sys.argv) > 1 else None)
