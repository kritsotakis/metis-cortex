#!/usr/bin/env python3
"""
Metis — Document Intake Pipeline (Prototype #3)

Drop a PDF in a matter's incoming folder. Run this tool. It will:

  1. Extract the document text (text-layer first via fitz; pdfplumber fallback)
  2. Categorise the document (SA letter / ATO letter / Court order / Bank
     statement / Other) using header-pattern heuristics
  3. Extract structured facts (sender, date, subject, key amounts, key
     reference numbers — CRN, ABN, ACN)
  4. Write a fact-extract markdown file into the matter's
     prior-application/ folder matching the existing `sa_*_received_*.md`
     pattern that Peter's DPO matter already uses
  5. Move the source PDF to prior-application/ alongside its extract
  6. Print a one-line PAIR.md entry suggestion for Peter to paste in

Scanned PDFs (no text layer) get a clear instruction message rather than
silent garbage output. Real OCR via Apple Vision Framework is Phase 2.

Usage:
  python3 intake.py <pdf_path> [<matter_folder>]

Defaults:
  matter_folder = ~/Desktop/child-support-stay-order

Examples:
  python3 intake.py ~/Downloads/sa-letter-2026-06-01.pdf
  python3 intake.py ~/Downloads/ato-noa-2024-25.pdf ~/Desktop/some-other-matter
"""

from __future__ import annotations

import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Text extraction — fitz first, pdfplumber fallback
# ---------------------------------------------------------------------------

def extract_text(pdf_path: Path) -> tuple[str, str]:
    """Return (full_text, extractor_name). Empty string if no text layer."""
    # fitz / PyMuPDF — fastest, most accurate
    try:
        import fitz  # type: ignore
        doc = fitz.open(str(pdf_path))
        parts = []
        for page in doc:
            parts.append(page.get_text("text"))
        doc.close()
        text = "\n".join(parts).strip()
        if text:
            return text, "fitz"
    except Exception as exc:
        print(f"   (fitz failed: {exc})", file=sys.stderr)
    # pdfplumber fallback
    try:
        import pdfplumber  # type: ignore
        with pdfplumber.open(str(pdf_path)) as pdf:
            parts = [(page.extract_text() or "") for page in pdf.pages]
        text = "\n".join(parts).strip()
        if text:
            return text, "pdfplumber"
    except Exception as exc:
        print(f"   (pdfplumber failed: {exc})", file=sys.stderr)
    return "", "none"


# ---------------------------------------------------------------------------
# Document categorisation — header-pattern heuristics
# ---------------------------------------------------------------------------

CATEGORIES = [
    # (id, friendly name, header patterns, default destination subfolder)
    (
        "sa_child_support",
        "Services Australia — Child Support",
        [r"services\s+australia", r"child\s+support", r"csaonline", r"\bCS\s+(?:assess|reference)\b"],
        "prior-application",
    ),
    (
        "ato",
        "ATO — Taxation",
        [r"australian\s+tax(?:ation)?\s+office", r"\bATO\b", r"notice\s+of\s+assessment", r"tax\s+return"],
        "prior-application",
    ),
    (
        "fcfcoa",
        "Federal Circuit and Family Court",
        [r"federal\s+circuit\s+and\s+family\s+court", r"\bFCFCOA\b", r"family\s+court\s+of\s+australia"],
        "prior-application",
    ),
    (
        "afsa",
        "AFSA — Insolvency",
        [r"australian\s+financial\s+security\s+authority", r"\bAFSA\b", r"bankruptcy", r"insolven"],
        "prior-application",
    ),
    (
        "asic",
        "ASIC — Companies",
        [r"australian\s+securities\s+and\s+investments\s+commission", r"\bASIC\b", r"company\s+extract"],
        "prior-application",
    ),
    (
        "bank_statement",
        "Bank — statement",
        [r"\b(NAB|ANZ|Westpac|Commonwealth\s+Bank|CommBank|St\.?George|Bendigo|Macquarie|ING)\b", r"account\s+statement", r"opening\s+balance"],
        "prior-application",
    ),
    (
        "legal_correspondence",
        "Legal correspondence",
        [r"\bRe:\s", r"acting\s+on\s+behalf", r"\bbarrister\b", r"\bsolicitor\b"],
        "prior-application",
    ),
    (
        "other",
        "Other / unclassified",
        [],
        "prior-application",
    ),
]


def categorise(text: str) -> tuple[str, str, str]:
    """Return (category_id, friendly_name, dest_subfolder)."""
    lower_head = text[:2500].lower()
    for cid, name, patterns, dest in CATEGORIES:
        for p in patterns:
            if re.search(p, lower_head, re.IGNORECASE):
                return cid, name, dest
    return "other", "Other / unclassified", "prior-application"


# ---------------------------------------------------------------------------
# Fact extraction — pattern-based
# ---------------------------------------------------------------------------

DATE_DMY = re.compile(
    r"\b([0-3]?[0-9]\s+(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+20[0-9]{2})\b"
)
DATE_ISO = re.compile(r"\b(20[0-9]{2}-[01][0-9]-[0-3][0-9])\b")
DOLLAR = re.compile(r"\$\s*[0-9]{1,3}(?:[,\s][0-9]{3})+(?:\.[0-9]{1,2})?")
ABN = re.compile(r"\bABN[:\s]+(\d{2}\s?\d{3}\s?\d{3}\s?\d{3})\b")
ACN = re.compile(r"\bACN[:\s]+(\d{3}\s?\d{3}\s?\d{3})\b")
CRN = re.compile(r"\b(?:CRN|Customer\s+Reference\s+(?:Number|No\.?))[:\s]+([0-9\s]{9,})\b", re.IGNORECASE)
CASE_NO = re.compile(r"\b(?:Case|File|Matter)\s+(?:No\.?|Number)[:\s]+([A-Z0-9/\-]+)\b", re.IGNORECASE)
SUBJECT = re.compile(r"(?:^|\n)\s*(?:Re|Subject|RE|SUBJECT):\s*([^\n]{5,200})", re.IGNORECASE)


def extract_facts(text: str) -> dict:
    facts: dict = {}
    # Subject / Re line
    m = SUBJECT.search(text)
    if m:
        facts["subject"] = m.group(1).strip().rstrip(".")
    # Dates
    dates = list(dict.fromkeys(DATE_DMY.findall(text) + DATE_ISO.findall(text)))
    if dates:
        facts["dates"] = dates[:10]
    # Dollar amounts
    amounts = list(dict.fromkeys(DOLLAR.findall(text)))
    if amounts:
        facts["dollar_amounts"] = amounts[:15]
    # Identifiers
    crns = list(dict.fromkeys(CRN.findall(text)))
    if crns:
        facts["customer_reference"] = [re.sub(r"\s+", "", c) for c in crns[:5]]
    abns = list(dict.fromkeys(ABN.findall(text)))
    if abns:
        facts["abns"] = abns[:5]
    acns = list(dict.fromkeys(ACN.findall(text)))
    if acns:
        facts["acns"] = acns[:5]
    case_nos = list(dict.fromkeys(CASE_NO.findall(text)))
    if case_nos:
        facts["case_numbers"] = case_nos[:5]
    return facts


# ---------------------------------------------------------------------------
# Markdown extract file generation
# ---------------------------------------------------------------------------

def render_extract(
    source_pdf: Path,
    pdf_dest_rel: str,
    text: str,
    extractor: str,
    cat_id: str,
    cat_name: str,
    facts: dict,
) -> str:
    today = date.today().isoformat()
    title_slug = cat_id.replace("_", "-")
    parts: list[str] = []
    parts.append(f"# Document intake — {cat_name}\n\n")
    parts.append(f"**Source PDF:** `{pdf_dest_rel}`\n")
    parts.append(f"**Original filename:** `{source_pdf.name}`\n")
    parts.append(f"**Intake date:** {today}\n")
    parts.append(f"**Category:** `{cat_id}` — {cat_name}\n")
    parts.append(f"**Text extractor used:** `{extractor}`\n")
    parts.append(f"**Text length:** {len(text):,} chars · {len(text.splitlines())} lines\n\n")
    parts.append("---\n\n")

    # Facts section
    if facts:
        parts.append("## Extracted facts\n\n")
        if "subject" in facts:
            parts.append(f"**Subject line:** {facts['subject']}\n\n")
        if "dates" in facts:
            parts.append(f"**Dates mentioned:** {' · '.join(facts['dates'])}\n\n")
        if "dollar_amounts" in facts:
            parts.append(f"**Dollar amounts:** {' · '.join(facts['dollar_amounts'])}\n\n")
        if "customer_reference" in facts:
            parts.append(f"**Customer Reference Number (CRN):** {' · '.join(facts['customer_reference'])}\n\n")
        if "abns" in facts:
            parts.append(f"**ABN(s):** {' · '.join(facts['abns'])}\n\n")
        if "acns" in facts:
            parts.append(f"**ACN(s):** {' · '.join(facts['acns'])}\n\n")
        if "case_numbers" in facts:
            parts.append(f"**Case / file / matter numbers:** {' · '.join(facts['case_numbers'])}\n\n")
        parts.append("---\n\n")
    else:
        parts.append("## Extracted facts\n\nNo structured facts auto-detected. Review the full text below.\n\n---\n\n")

    # Notes for Peter
    parts.append("## Next actions (suggested)\n\n")
    if cat_id == "sa_child_support":
        parts.append("- This is Services Australia correspondence. Check whether it relates to:\n")
        parts.append("  - the existing DPO matter — file under `prior-application/`\n")
        parts.append("  - Sarah's June 2026 Change of Assessment — extract relevant facts into the `06_sa_response_to_sarah_coa_2026-06-15.md` draft\n")
        parts.append("  - a NEW matter — create new fact-extract category\n")
        parts.append("- Update PAIR.md with a one-line entry referencing this intake\n")
        parts.append("- Re-run consistency_checker.py to re-cross-reference new facts against existing drafts\n\n")
    elif cat_id == "ato":
        parts.append("- This is ATO correspondence. Check whether it relates to:\n")
        parts.append("  - 2019-20 income year — reconcile with affidavit Para 11 (`$327,016` ATI)\n")
        parts.append("  - DSK income lodgement — closes REDLINE F16\n")
        parts.append("  - Any other tax year — file for cross-reference\n\n")
    elif cat_id == "fcfcoa":
        parts.append("- This is FCFCOA correspondence. Likely a sealed order, listing notice, or registry communication.\n")
        parts.append("- File under prior-application AND add to PAIR.md action queue if it requires response.\n\n")
    elif cat_id == "afsa":
        parts.append("- This is AFSA / bankruptcy correspondence. Coordinate with Alice Russell (Wesley).\n\n")
    else:
        parts.append(f"- This document was categorised as **{cat_name}**.\n")
        parts.append("- Review the extracted text below + add to PAIR.md if action required.\n\n")

    # Full extracted text
    parts.append("---\n\n## Full extracted text\n\n```\n")
    parts.append(text)
    parts.append("\n```\n")

    return "".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if len(sys.argv) < 2:
        print("usage: intake.py <pdf_path> [<matter_folder>]", file=sys.stderr)
        return 2

    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.is_file():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 2
    if pdf_path.suffix.lower() != ".pdf":
        print(f"warning: file extension is not .pdf — proceeding anyway: {pdf_path.suffix}", file=sys.stderr)

    matter_root = (
        Path(sys.argv[2]).expanduser().resolve()
        if len(sys.argv) >= 3
        else Path.home() / "Desktop/child-support-stay-order"
    )
    if not matter_root.is_dir():
        print(f"matter folder not found: {matter_root}", file=sys.stderr)
        return 2

    print(f"intake: {pdf_path.name}")
    print(f"matter: {matter_root}")

    # 1. Extract text
    text, extractor = extract_text(pdf_path)
    if not text or len(text) < 50:
        ocr_out = pdf_path.with_suffix(".ocr.pdf")
        print("\n❌ No usable text layer found in this PDF.\n")
        print("This is most likely a scanned image PDF. Two options:")
        print("  (a) Open the PDF in macOS Preview → File → Export → check 'Text' option → save as a new PDF. Then re-run intake.py on the new file.")
        print("  (b) Use a tool like 'ocrmypdf' (brew install ocrmypdf) to add a text layer:")
        print(f"      ocrmypdf '{pdf_path}' '{ocr_out}'")
        print("\nReal OCR via Apple Vision Framework will be added in Phase 2 of Metis.\n")
        return 1
    print(f"text-layer extracted via {extractor}: {len(text):,} chars")

    # 2. Categorise
    cat_id, cat_name, dest_subfolder = categorise(text)
    print(f"category: {cat_name} ({cat_id})")

    # 3. Extract facts
    facts = extract_facts(text)
    print(f"facts: {', '.join(facts.keys()) if facts else 'none auto-detected'}")

    # 4. Compose destination paths
    today = date.today().isoformat()
    safe_orig = re.sub(r"[^A-Za-z0-9._\-]+", "_", pdf_path.stem)[:80]
    pdf_dest_dir = matter_root / dest_subfolder
    pdf_dest_dir.mkdir(parents=True, exist_ok=True)
    pdf_dest = pdf_dest_dir / f"{today}_{safe_orig}.pdf"
    extract_dest = pdf_dest_dir / f"{cat_id}_received_{today}_{safe_orig}.md"

    # If a file with the same name already exists, append a counter
    counter = 1
    while pdf_dest.exists() or extract_dest.exists():
        pdf_dest = pdf_dest_dir / f"{today}_{safe_orig}_{counter}.pdf"
        extract_dest = pdf_dest_dir / f"{cat_id}_received_{today}_{safe_orig}_{counter}.md"
        counter += 1

    # 5. Copy PDF (don't move — keep original safe)
    shutil.copy2(pdf_path, pdf_dest)
    pdf_dest_rel = pdf_dest.relative_to(matter_root).as_posix()
    print(f"PDF copied to: {pdf_dest_rel}")

    # 6. Write extract markdown
    extract_md = render_extract(pdf_path, pdf_dest_rel, text, extractor, cat_id, cat_name, facts)
    extract_dest.write_text(extract_md, encoding="utf-8")
    extract_rel = extract_dest.relative_to(matter_root).as_posix()
    print(f"extract written: {extract_rel}")

    # 7. Suggest PAIR.md entry
    print(f"\n--- Suggested PAIR.md entry (paste into ~/Desktop/child-support-stay-order/PAIR.md) ---")
    print(f"### {today} — metis intake → log")
    print(f"**Did:** Intake of {pdf_path.name}. Categorised as {cat_name}. Text extract + fact summary at `{extract_rel}`; PDF at `{pdf_dest_rel}`.")
    if facts:
        keys = [k for k in ["subject", "dates", "customer_reference", "dollar_amounts"] if k in facts]
        if keys:
            print(f"**Facts surfaced:** {', '.join(keys)}.")
    print(f"**Need from peter:** review + update PAIR.md action queue if response required.")
    print(f"**Status:** 🟢 done (intake) / awaits Peter classification")

    return 0


if __name__ == "__main__":
    sys.exit(main())
