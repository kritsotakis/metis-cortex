"""
UPL safe-harbour rails — SYSTEM-ENFORCED, not left to model discretion.

Source: METIS-CLIENT-WORKFLOW-SPEC.md UPL architecture +
METIS-REDTEAM-LIVE-LAW-2026-06-26.md (the red-team showed the raw model
happily produces advice-shaped output; these rails are the product).

Three layers:
  1. SYSTEM_PROMPT — instructs the model (necessary, not sufficient)
  2. check_output() — advice-shape detector on every model output
  3. watermark() — every exported artefact carries the DRAFT banner
"""

from __future__ import annotations

import re

DISCLAIMER = (
    "Metis is a document-organisation and drafting assistant. "
    "It is not a law firm and does not provide legal advice."
)

DRAFT_BANNER = "DRAFT — FOR REVIEW BY YOUR SOLICITOR"

LAWYER_FLAG = (
    "⚖️  This is a legal call, not documentation. Discuss with your solicitor "
    "(or book a duty-lawyer consult) before deciding."
)

SYSTEM_PROMPT = f"""You are Metis, a document-organisation co-pilot for ONE user's own
Australian family-law matter. The user is self-represented and is the matter owner.

HARD RULES — never break these:
1. DOMAIN LOCK: you assist ONLY with organising THIS Australian family-law matter
   (documents, chronology, checklists, drafts). Any other topic — other areas of law,
   tax advice, financial advice, anything outside this matter — answer exactly:
   "That's outside what Metis does. Metis only helps organise this family-law matter."
2. NO ADVICE: never recommend a course of action, predict an outcome, rank options
   as a recommendation, or say what the user "should" do. You may DESCRIBE options
   and their documented trade-offs, then flag the choice to the solicitor.
3. Every strategic fork ends with: "{LAWYER_FLAG}"
4. Every draft or document text you produce is headed: "{DRAFT_BANNER}"
5. TAX RAIL: you may identify and file tax documents ("this is your 2019-20 NOA
   showing ATI $X"). You must never interpret tax positions or their consequences —
   that is tax-agent territory.
6. No opinion sentences about legal merits without citing the source document
   in the matter folder that supports the statement.
"""

# Advice-shape detector — patterns that indicate the output crossed the line.
_ADVICE_PATTERNS = [
    r"\byou should\b",
    r"\bI (?:recommend|advise|suggest you)\b",
    r"\bmy recommendation\b",
    r"\bthe best (?:option|choice|path|course)\b",
    r"\byou(?:'ll| will) (?:win|lose|succeed|fail)\b",
    r"\blikely to (?:win|lose|succeed)\b",
    r"\byour best bet\b",
    r"\bgo with option\b",
    r"\bI would (?:choose|pick|go with)\b",
]
_ADVICE_RE = re.compile("|".join(_ADVICE_PATTERNS), re.IGNORECASE)


def check_output(text: str) -> tuple[bool, list[str]]:
    """Return (ok, violations). ok=False means the output is advice-shaped."""
    violations = [m.group(0) for m in _ADVICE_RE.finditer(text)]
    return (not violations, violations)


def enforce(text: str) -> str:
    """Gate model output: pass clean text through; block advice-shaped text."""
    ok, violations = check_output(text)
    if ok:
        return text
    return (
        "⛔ Metis withheld part of this response because it crossed into "
        f"recommendation territory ({', '.join(set(violations))!s}). "
        "Metis organises; your solicitor advises.\n\n" + LAWYER_FLAG
    )


def watermark(document_text: str) -> str:
    """Every exported artefact carries the banner + disclaimer."""
    return f"**{DRAFT_BANNER}**\n\n{document_text}\n\n---\n*{DISCLAIMER}*"
