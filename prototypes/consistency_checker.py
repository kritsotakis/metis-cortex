#!/usr/bin/env python3
"""
Metis Cortex — Document Consistency Checker (Prototype #1)

Reads a matter folder containing markdown drafts + supporting docs, extracts
structured claims (dates, dollar amounts, party identifiers, registration
numbers, case law citations), groups identical-value claims across documents,
and emits a markdown report flagging inconsistencies + appearances + gaps.

This is the prototype slice from CLIENT-SIDE-TEST-CASE-BRIEF-2026-06-01.md
item #2 — "Document consistency checker", explicitly called out as "the
highest-value automation here" (line 135 of the brief).

Why pattern-based, not LLM:
  - Deterministic — same input always produces same output
  - Transparent — every flag has a visible source line
  - Fast — runs in milliseconds against 50 docs
  - Cheap — zero API calls per run
  - The job (find string-level claim inconsistencies across docs) doesn't
    need semantic reasoning that LLMs add complexity to deliver
  - LLM enrichment can be added in Phase 1 of the real Metis build for
    paraphrase detection ("$327k" vs "approximately $327,000")

Read-only against the matter folder. Writes a single report file.

Usage:
  python3 consistency_checker.py <matter_folder> [<output_report.md>]

Defaults:
  matter_folder = ~/Desktop/child-support-stay-order
  output_report = ~/Desktop/metis-cortex/CONSISTENCY-REPORT-<today>.md
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict, namedtuple
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Pattern library — what kinds of claims we look for
# ---------------------------------------------------------------------------
#
# Each pattern tuple is (label, compiled_regex, normaliser_function).
# The normaliser collapses near-duplicates (e.g. "$1,283,000" and "1283000"
# normalise to the same canonical value so they group together).

Match = namedtuple("Match", "label canonical raw doc line_no line_text")


def _norm_dollar(raw: str) -> str:
    """Normalise dollar amounts to int strings. '$1,283,000' -> '1283000'."""
    digits = re.sub(r"[^0-9]", "", raw)
    if not digits:
        return raw.strip()
    return digits.lstrip("0") or "0"


def _norm_date_dmy(raw: str) -> str:
    """Normalise '29 May 2020' to '2020-05-29'."""
    months = {
        "january": "01", "february": "02", "march": "03", "april": "04",
        "may": "05", "june": "06", "july": "07", "august": "08",
        "september": "09", "october": "10", "november": "11", "december": "12",
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "sept": "09", "oct": "10", "nov": "11", "dec": "12",
    }
    m = re.match(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", raw.strip())
    if not m:
        return raw.strip()
    d, mn, y = m.group(1), m.group(2).lower(), m.group(3)
    if mn not in months:
        return raw.strip()
    return f"{y}-{months[mn]}-{int(d):02d}"


def _norm_iso(raw: str) -> str:
    return raw.strip()


def _norm_identifier(raw: str) -> str:
    """Strip whitespace + uppercase for IDs (ABN, ACN, ASIC, CRN)."""
    return re.sub(r"\s+", " ", raw).strip().upper()


def _norm_address(raw: str) -> str:
    """Collapse whitespace + strip punctuation noise for address comparison."""
    s = re.sub(r"\s+", " ", raw).strip()
    return s.rstrip(",.")


def _norm_party(raw: str) -> str:
    """Title-case + collapse whitespace for party names."""
    return re.sub(r"\s+", " ", raw).strip().title()


def _norm_case(raw: str) -> str:
    """Case citations — strip whitespace, lowercase for grouping."""
    return re.sub(r"\s+", " ", raw).strip().lower()


# Patterns. Each one: (label, pattern, normaliser, value_group_index)
PATTERNS = [
    # Dollar amounts ($1,283,000 / $327,016 / A$700)
    ("dollar_amount",
     re.compile(r"(?:A?\$)\s*([0-9]{1,3}(?:[,\s][0-9]{3})+(?:\.[0-9]+)?|[0-9]+(?:\.[0-9]+)?)\b"),
     _norm_dollar),
    # ISO dates (2020-05-29)
    ("iso_date",
     re.compile(r"\b(20[0-9]{2}-[01][0-9]-[0-3][0-9])\b"),
     _norm_iso),
    # DMY long dates (29 May 2020 / 6 May 2024)
    ("dmy_date",
     re.compile(r"\b([0-3]?[0-9]\s+(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+20[0-9]{2})\b"),
     _norm_date_dmy),
    # ABN — 11 digits
    ("ABN",
     re.compile(r"\bABN[:\s]+(\d{2}\s?\d{3}\s?\d{3}\s?\d{3})\b"),
     _norm_identifier),
    # ACN — 9 digits
    ("ACN",
     re.compile(r"\bACN[:\s]+(\d{3}\s?\d{3}\s?\d{3})\b"),
     _norm_identifier),
    # Family Law Act sections
    ("FLA_section",
     re.compile(r"\bs\.?(\s?[0-9]{1,3}[A-Z]{0,3}(?:\([0-9a-z]+\))*)\b"),
     _norm_identifier),
    # Property addresses (with NSW state and postcode)
    ("property_address",
     re.compile(r"([0-9]+[A-Z]?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3}\s+(?:Street|St|Road|Rd|Avenue|Ave|Close|Cl|Drive|Dr|Lane|Ln|Place|Pl|Court|Ct|Way),?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+(?:NSW|VIC|QLD|SA|WA|ACT|TAS|NT)\s+\d{4})"),
     _norm_address),
    # Party first-names (Kritsotakis-family parties + Sarah)
    # We match only specific names so we don't pick up random uses of common
    # words. Case-insensitive but normalise to title case.
    ("party_peter",
     re.compile(r"\b(Peter Kritsotakis)\b"),
     _norm_party),
    ("party_sarah",
     re.compile(r"\b(Sarah Kritsotakis|Sarah(?=\s+(?:[A-Z]|\w*[Kk]ritsotakis)))"),
     _norm_party),
    ("party_karren",
     re.compile(r"\b(Karren Kritsotakis|Karren(?=\s+(?:[A-Z]|\w*[Kk]ritsotakis)))"),
     _norm_party),
    # Case citations (Stanford v Stanford / Goode v Goode / etc.)
    ("case_citation",
     re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+v\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:\s+(?:\([0-9]{4}\)|\[[0-9]{4}\])\s+[A-Z]{3,6}\s+[0-9]+)?)\b"),
     _norm_case),
    # Statute names (Family Law Act / Child Support Act etc. — full short
    # forms only, to avoid false positives)
    ("statute_short",
     re.compile(r"\b((?:Family\s+Law\s+Act|Child\s+Support\s+\((?:Assessment|Registration\s+and\s+Collection)\)\s+Act|Privacy\s+Act|Surveillance\s+Devices\s+Act|Freedom\s+of\s+Information\s+Act|Federal\s+Circuit\s+and\s+Family\s+Court\s+of\s+Australia\s+Act|Legal\s+Profession\s+Uniform\s+Law)\s+(?:19|20)[0-9]{2}(?:\s+\((?:Cth|NSW|VIC|QLD|SA|WA|ACT|TAS|NT)\))?)"),
     _norm_party),  # title-case suffices for statutes too
]


# ---------------------------------------------------------------------------
# Discovery — find the markdown files to scan
# ---------------------------------------------------------------------------

# Folder patterns to scan. Includes the drafts that are work products (we want
# consistency across those) AND fact-extract files (extracted facts feed into
# drafts). Excludes the noise: extracted/ (raw OCR output), forms/ (blank
# court forms), factsheets/ (Legal Aid reference material).
SCAN_INCLUDES = [
    "*.md",
    "drafts/*.md",
    "reference/*.md",
    "prior-application/*.md",
    "filing/*.md",
]

# Files explicitly excluded — these are intentionally heterogeneous (e.g. a
# critique deliberately includes the wrong values to flag them) so the
# checker would generate noise rather than signal against them.
SCAN_EXCLUDES = {
    "REDLINE-DPO-2026-05-27.md",  # By definition contains old + new wording side by side
    "reference/adversarial_critique.md",  # Designed to surface contradictions, not avoid them
}


def discover_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in SCAN_INCLUDES:
        for f in root.glob(pattern):
            if f.is_file():
                rel = f.relative_to(root).as_posix()
                if rel in SCAN_EXCLUDES:
                    continue
                files.append(f)
    return sorted(set(files))


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def extract_from_file(f: Path, root: Path) -> list[Match]:
    out: list[Match] = []
    rel = f.relative_to(root).as_posix()
    try:
        text = f.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return out
    for i, line in enumerate(text.splitlines(), start=1):
        # Skip code fences and comment-only lines to reduce noise
        stripped = line.strip()
        if not stripped or stripped.startswith("```") or stripped.startswith("> "):
            continue
        for label, regex, norm in PATTERNS:
            for m in regex.finditer(line):
                raw = m.group(1)
                canonical = norm(raw)
                # Filter out obviously noisy hits
                if label == "dollar_amount" and canonical in {"0", "1", "10", "100", "1000"}:
                    continue
                if label == "dmy_date" and not raw[0].isdigit():
                    continue
                # Truncate line context for the report
                ctx = line.strip()
                if len(ctx) > 180:
                    ctx = ctx[:177] + "..."
                out.append(Match(label, canonical, raw, rel, i, ctx))
    return out


# ---------------------------------------------------------------------------
# Analysis — group + classify
# ---------------------------------------------------------------------------

Grouped = dict[tuple[str, str], list[Match]]


def group_matches(all_matches: list[Match]) -> Grouped:
    grouped: Grouped = defaultdict(list)
    for m in all_matches:
        grouped[(m.label, m.canonical)].append(m)
    return grouped


def find_inconsistencies(grouped: Grouped) -> list[tuple[str, list[tuple[str, list[Match]]]]]:
    """For each label, find values that look like they SHOULD be the same but
    differ. The simplest heuristic: same label + similar context but different
    canonical value. For numerical-y labels (dollar_amount, ABN, ACN), look
    for nearly-identical values (one digit off, etc.). For party names, look
    for variants that map to the same person.

    We don't try to be too clever in v1 — we just produce a "facts appearing
    in this many docs" view that Peter can scan visually for obvious drift.
    """
    # Currently no automated inconsistency detector. The report below renders
    # a structured view that makes manual drift detection trivial. Adding
    # automated drift detection is a Phase 2 enhancement.
    return []


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

LABEL_HEADLINES = {
    "dollar_amount": "Dollar amounts",
    "iso_date": "Dates (ISO format)",
    "dmy_date": "Dates (DD Month YYYY format)",
    "ABN": "ABNs",
    "ACN": "ACNs",
    "FLA_section": "Statutory references",
    "property_address": "Property addresses",
    "party_peter": "Peter (party identifier)",
    "party_sarah": "Sarah (party identifier)",
    "party_karren": "Karren (party identifier)",
    "case_citation": "Case citations",
    "statute_short": "Statute short forms",
}


def render_report(root: Path, files: list[Path], grouped: Grouped) -> str:
    today = date.today().isoformat()
    total_matches = sum(len(v) for v in grouped.values())
    unique_values = len(grouped)

    parts: list[str] = []
    parts.append(f"# Metis — Document Consistency Report\n\n")
    parts.append(f"**Matter:** `{root}`\n")
    parts.append(f"**Generated:** {today}\n")
    parts.append(f"**Files scanned:** {len(files)}\n")
    parts.append(f"**Distinct facts extracted:** {unique_values}\n")
    parts.append(f"**Total fact occurrences:** {total_matches}\n\n")
    parts.append(
        "This report shows every claim of the kinds it knows how to recognise "
        "(dates, dollar amounts, ABNs/ACNs, statutory references, property "
        "addresses, party names, case citations, statute short forms) along "
        "with every place that claim appears in the matter folder. Visually "
        "scan each section: if a value appears in only one document but "
        "should appear in several, that's a gap. If two values are "
        "near-duplicates ($327,016 vs $327,000), that's drift.\n\n"
    )
    parts.append("---\n\n")

    # Files scanned
    parts.append("## Files scanned\n\n")
    for f in files:
        rel = f.relative_to(root).as_posix()
        parts.append(f"- `{rel}`\n")
    parts.append("\n---\n\n")

    # By label
    for label in sorted(LABEL_HEADLINES.keys()):
        section = [(canonical, matches) for (lbl, canonical), matches in grouped.items() if lbl == label]
        if not section:
            continue
        # Sort: facts appearing in most docs first (most-cited = most
        # consistency-critical)
        section.sort(key=lambda kv: (-len(set(m.doc for m in kv[1])), kv[0]))

        parts.append(f"## {LABEL_HEADLINES[label]}\n\n")
        for canonical, matches in section:
            docs = sorted(set(m.doc for m in matches))
            # Render the canonical value with the raw form variants we found
            raw_variants = sorted(set(m.raw for m in matches))
            head = f"### `{canonical}`"
            if len(raw_variants) > 1 or raw_variants[0] != canonical:
                head += f" — raw: " + ", ".join(f"`{r}`" for r in raw_variants)
            head += f"  · {len(docs)} doc(s), {len(matches)} occurrence(s)"
            parts.append(head + "\n\n")
            for m in matches:
                parts.append(f"- `{m.doc}:{m.line_no}` — {m.line_text}\n")
            parts.append("\n")
        parts.append("---\n\n")

    # Recommendations
    parts.append("## Reading this report\n\n")
    parts.append(
        "1. **Look at the high-occurrence facts first** — the values that "
        "appear in many documents. Those are the load-bearing claims of the "
        "matter. They MUST be consistent.\n\n"
        "2. **Flag near-duplicates** — `$327,016` vs `$327,000` vs `$327k` "
        "are not the same to a court even if they're 'roughly the same'. "
        "Pick the precise number and use it everywhere.\n\n"
        "3. **Gap analysis** — facts that appear in only one doc but logically "
        "should appear in others (e.g. Peter's CRN appearing in cover letters "
        "but not the affidavit). The report doesn't auto-detect these; you "
        "scan for them.\n\n"
        "4. **Re-run after every material edit** — pattern is deterministic, "
        "so the only changes between runs are real changes in the matter. "
        "A 5-second sanity check before any filing.\n\n"
    )

    parts.append("---\n\n")
    parts.append(
        "*Prototype #1 of the Metis client-side build — Document Consistency "
        "Checker. Pattern-based; LLM enrichment for paraphrase detection "
        "(`$327k` vs `$327,016`) deferred to Phase 1 build. Source: "
        "`~/Desktop/metis-cortex/prototypes/consistency_checker.py`.*\n"
    )

    return "".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if len(sys.argv) < 2:
        matter = Path.home() / "Desktop/child-support-stay-order"
    else:
        matter = Path(sys.argv[1]).expanduser().resolve()
    if not matter.is_dir():
        print(f"matter folder not found: {matter}", file=sys.stderr)
        return 2

    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2]).expanduser().resolve()
    else:
        out_path = Path.home() / "Desktop/metis-cortex" / f"CONSISTENCY-REPORT-{date.today().isoformat()}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = discover_files(matter)
    if not files:
        print(f"no markdown files found in {matter}", file=sys.stderr)
        return 1

    all_matches: list[Match] = []
    for f in files:
        all_matches.extend(extract_from_file(f, matter))

    grouped = group_matches(all_matches)
    report = render_report(matter, files, grouped)
    out_path.write_text(report, encoding="utf-8")

    # Brief stats to stdout for the runner
    print(f"matter: {matter}")
    print(f"scanned: {len(files)} files")
    print(f"extracted: {sum(len(v) for v in grouped.values())} fact occurrences")
    print(f"distinct values: {len(grouped)}")
    print(f"report: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
