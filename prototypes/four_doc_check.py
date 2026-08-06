#!/usr/bin/env python3
"""
Metis — 4-Document Consistency Reconciliation (Prototype #4)

Validates factual consistency across the four documents that must tell
ONE coherent story in Peter's matter:

  1. SA Response to Sarah's Reason 8B Change of Assessment (due 15 Jun 2026)
  2. FCFCOA Initiating Application + Affidavit
  3. FCFCOA Financial Statement
  4. Bankruptcy Statement of Affairs

The DPO session flagged 4-doc consistency reconciliation as the highest-pain
item — drift across these documents = catastrophic credibility damage in any
one of them, AND potential perjury/clawback exposure.

This tool is the read-only product slice the DPO session asked for as
"product-validation in real conditions".

Architecture:
  - Pattern-based, deterministic
  - Read-only against matter folder
  - Outputs structured markdown report:
    - documents present/missing
    - field × doc matrix (✓/✗/✗ expected)
    - cross-doc consistency check (mismatch flags)
    - gap analysis per doc (fields expected but absent)

Usage:
  python3 four_doc_check.py [<matter_folder>] [<output_report>]

Defaults:
  matter_folder = ~/Desktop/child-support-stay-order
  output_report = ~/Desktop/metis-cortex/RECONCILIATION-REPORT-<today>.md
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# The four documents — discovery patterns + expected fields per doc
# ---------------------------------------------------------------------------

DOCS = [
    {
        "id": "sa_response",
        "label": "SA Response (Sarah's Reason 8B COA)",
        "discovery_patterns": [
            "drafts/06_sa_response_to_sarah_coa_*.md",
            "drafts/*sa_response*.md",
            "drafts/*sarah_coa*.md",
        ],
        # The COA response should disclose Peter's income + capacity in detail
        # to rebut the earning-capacity claim
        "expected_fields": [
            "current_income", "income_history_5yr", "workers_comp_status",
            "dsk_income", "asset_pool_overview", "tempe_sale_disposition",
            "peter_crn", "sarah_full_name", "children_names",
            "fv_screening_outcome",
        ],
    },
    {
        "id": "fcfcoa_init_app",
        "label": "FCFCOA Initiating Application",
        "discovery_patterns": [
            "drafts/01_initiating_application*.md",
            "drafts/01_initiating*.md",
        ],
        "expected_fields": [
            "peter_full_name", "sarah_full_name", "children_names",
            "orders_sought", "case_number_assigned",
        ],
    },
    {
        "id": "fcfcoa_affidavit",
        "label": "FCFCOA Affidavit",
        "discovery_patterns": [
            "drafts/02_affidavit.md",
            "drafts/02_affidavit*.md",
        ],
        # The affidavit is the comprehensive disclosure backbone
        "expected_fields": [
            "peter_full_name", "peter_address", "peter_dob", "peter_crn",
            "sarah_full_name", "children_names",
            "income_2019_20_ati", "income_2019_20_cgt_component",
            "income_other_years_summary",
            "tempe_property_address", "tempe_sale_price", "tempe_sale_date",
            "tempe_proceeds_breakdown",
            "current_income_workers_comp", "current_income_dsk",
            "trust_abn", "trust_role",
            "pty_ltd_acn", "pty_ltd_role", "pty_ltd_shares",
            "ftx_deposit_amount", "ftx_deposit_status",
            "parents_loan_amount",
            "dpo_date_issued", "dpo_delegate", "service_method",
            "sa_rejection_letter_date", "sa_rejection_reason_98c",
            "bankruptcy_status",
            "fv_screening_outcome",
        ],
    },
    {
        "id": "fcfcoa_financial_statement",
        "label": "FCFCOA Financial Statement",
        "discovery_patterns": [
            "drafts/*financial_statement*.md",
            "filled/*financial_statement*",
            "forms/*financial_statement*",
        ],
        "expected_fields": [
            "peter_full_name", "peter_address", "peter_dob",
            "income_total_weekly_gross", "income_total_weekly_net",
            "asset_pool_total", "liability_pool_total",
            "trust_abn", "pty_ltd_acn", "pty_ltd_shares",
            "current_income_workers_comp", "current_income_dsk",
        ],
    },
    {
        "id": "bankruptcy_soa",
        "label": "Bankruptcy Statement of Affairs",
        "discovery_patterns": [
            "drafts/*bankruptcy*statement*",
            "drafts/*statement_of_affairs*",
            "drafts/05_email_alice_russell_bankruptcy*.md",  # email coord doc
        ],
        "expected_fields": [
            "peter_full_name", "peter_address", "peter_dob",
            "asset_pool_total", "liability_pool_total",
            "creditors_list",
            "trust_abn", "pty_ltd_acn", "pty_ltd_shares",
        ],
    },
]


# ---------------------------------------------------------------------------
# Field extractors — pattern-based, per-field
# ---------------------------------------------------------------------------

# Each field has: an extraction regex (or list) returning a value, and a
# canonicaliser that normalises for cross-doc comparison.

def _norm_dollar(s: str) -> str:
    digits = re.sub(r"[^0-9]", "", s)
    return digits.lstrip("0") or "0"


def _norm_date(s: str) -> str:
    months = {
        "january": "01", "february": "02", "march": "03", "april": "04",
        "may": "05", "june": "06", "july": "07", "august": "08",
        "september": "09", "october": "10", "november": "11", "december": "12",
    }
    iso = re.match(r"(\d{4})-(\d{2})-(\d{2})", s.strip())
    if iso:
        return s.strip()[:10]
    dmy = re.match(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", s.strip())
    if dmy:
        d, m, y = dmy.group(1), dmy.group(2).lower(), dmy.group(3)
        if m in months:
            return f"{y}-{months[m]}-{int(d):02d}"
    return s.strip()


def _norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().rstrip(".")


def _norm_id(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().upper()


FIELD_EXTRACTORS = {
    "peter_full_name": {
        "label": "Peter's full name",
        "patterns": [r"\b(Peter\s+Kritsotakis)\b"],
        "norm": _norm_text,
    },
    "peter_address": {
        "label": "Peter's residential address",
        "patterns": [
            r"(1\s+Oxford\s+Close[^\n\r,.]*[,\s]+Belrose[,\s]+NSW[,\s]+\d{4})",
        ],
        "norm": _norm_text,
    },
    "peter_dob": {
        "label": "Peter's DOB",
        "patterns": [
            r"(?:date\s+of\s+birth|DOB|born)[:\s]+(\d{1,2}\s+\w+\s+\d{4}|\d{4}-\d{2}-\d{2})",
        ],
        "norm": _norm_date,
    },
    "peter_crn": {
        "label": "Peter's Child Support CRN",
        "patterns": [
            r"\b(?:CRN|Customer\s+Reference\s+(?:Number|No\.?))[:\s]+([0-9\s]{9,})",
        ],
        "norm": lambda s: re.sub(r"\s+", "", s),
    },
    "sarah_full_name": {
        "label": "Sarah's full name",
        "patterns": [r"\b(Sarah\s+Kritsotakis)\b"],
        "norm": _norm_text,
    },
    "children_names": {
        "label": "Children's names",
        "patterns": [r"\b(Dimitri|Salvatore|Katerina)\b"],
        "norm": _norm_text,
        "multi": True,  # collect all matches
    },
    "income_2019_20_ati": {
        "label": "2019-20 Adjusted Taxable Income",
        "patterns": [
            r"2019[-–]20[^\n]{0,400}?ATI[^\n]{0,80}?\$\s*([0-9,]+)",
            r"ATI[^\n]{0,80}?\$\s*([0-9,]+)[^\n]{0,80}?2019[-–]20",
        ],
        "norm": _norm_dollar,
    },
    "income_2019_20_cgt_component": {
        "label": "2019-20 capital gain component (Tempe CGT)",
        "patterns": [
            r"(?:capital\s+gain|CGT)[^\n]{0,200}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]+)[^\n]{0,80}?(?:capital\s+gain|CGT)",
        ],
        "norm": _norm_dollar,
    },
    "tempe_property_address": {
        "label": "Tempe property address",
        "patterns": [
            r"(23\s+Lymerston\s+(?:St(?:reet)?)[^\n]{0,80}?(?:Tempe[^\n]{0,80}?2044|2044))",
            r"\b(23\s+Lymerston\s+St(?:reet)?)\b",
        ],
        "norm": _norm_text,
    },
    "tempe_sale_price": {
        "label": "Tempe sale price (gross)",
        "patterns": [
            r"Tempe[^\n]{0,300}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]{7,})[^\n]{0,300}?Tempe",
        ],
        "norm": _norm_dollar,
    },
    "tempe_sale_date": {
        "label": "Tempe settlement date",
        "patterns": [
            r"Tempe[^\n]{0,200}?(\d{1,2}\s+\w+\s+\d{4}|\d{4}-\d{2}-\d{2})",
            r"(29\s+May\s+2020)",
        ],
        "norm": _norm_date,
    },
    "tempe_proceeds_breakdown": {
        "label": "Tempe net proceeds breakdown (presence flag)",
        "patterns": [
            r"(net\s+proceeds[^\n]{0,200}(?:mortgage|FTX|FX|residual))",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "current_income_workers_comp": {
        "label": "Current workers compensation income",
        "patterns": [
            r"workers?\s+(?:comp(?:ensation)?)[^\n]{0,200}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]+)[^\n]{0,80}?(?:per\s+week|/wk|weekly)[^\n]{0,80}?workers?",
        ],
        "norm": _norm_dollar,
    },
    "current_income_dsk": {
        "label": "Current DSK business income",
        "patterns": [
            r"DSK[^\n]{0,250}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]+)[^\n]{0,200}?DSK",
            r"Detailing\s+Solutions\s+Krew[^\n]{0,250}?\$\s*([0-9,]+)",
        ],
        "norm": _norm_dollar,
    },
    "trust_abn": {
        "label": "Kritsotakis Family Trust ABN",
        "patterns": [r"\bABN[:\s]+(45\s?984\s?876\s?899)\b"],
        "norm": _norm_id,
    },
    "trust_role": {
        "label": "Peter's role in Kritsotakis Family Trust (presence)",
        "patterns": [r"(discretionary\s+beneficiary|named\s+beneficiary)"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "pty_ltd_acn": {
        "label": "Kritsotakis Investments Pty Ltd ACN",
        "patterns": [r"\bACN[:\s]+(153\s?844\s?136)\b"],
        "norm": _norm_id,
    },
    "pty_ltd_role": {
        "label": "Pty Ltd directorship / role disclosure (presence)",
        "patterns": [
            r"(?:Karren\s+Kritsotakis|sole\s+director)[^\n]{0,200}?Pty\s+Ltd",
            r"Pty\s+Ltd[^\n]{0,200}?(?:Karren\s+Kritsotakis|sole\s+director)",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "pty_ltd_shares": {
        "label": "Pty Ltd Peter shareholding",
        "patterns": [
            r"(100\s+partially[-\s]paid\s+ordinary\s+shares?)",
            r"(100[^\n]{0,80}?partially[-\s]paid)",
        ],
        "norm": _norm_text,
    },
    "ftx_deposit_amount": {
        "label": "FTX deposit amount",
        "patterns": [
            r"FTX[^\n]{0,200}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]+)[^\n]{0,80}?FTX",
        ],
        "norm": _norm_dollar,
    },
    "ftx_deposit_status": {
        "label": "FTX deposit status flag",
        "patterns": [
            r"(FTX[^\n]{0,200}(?:collapse|lost|2022))",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "parents_loan_amount": {
        "label": "Parents (Jim+Karren) loan amount",
        "patterns": [
            r"(?:Jim|Karren|parents)[^\n]{0,300}?\$\s*([0-9,]+)",
            r"\$\s*([0-9,]+)[^\n]{0,80}?(?:Jim|Karren|parents)",
        ],
        "norm": _norm_dollar,
    },
    "dpo_date_issued": {
        "label": "DPO date issued",
        "patterns": [
            r"(?:DPO|Departure\s+Prohibition\s+Order)[^\n]{0,300}?(\d{1,2}\s+\w+\s+202[0-9])",
            r"(23\s+December\s+2024)",
        ],
        "norm": _norm_date,
    },
    "sa_rejection_letter_date": {
        "label": "SA rejection letter date (re April 2025 COA)",
        "patterns": [
            r"(1\s+July\s+2025)",
            r"(?:rejection|rejected)[^\n]{0,200}?(\d{1,2}\s+\w+\s+2025)",
        ],
        "norm": _norm_date,
    },
    "sa_rejection_reason_98c": {
        "label": "SA rejection on s.98C 18-month limitation",
        "patterns": [r"(s\.?\s*98C|s98C|18[-\s]month)"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "bankruptcy_status": {
        "label": "Bankruptcy petition status flag",
        "patterns": [
            r"(bankruptcy[^\n]{0,200}(?:filing|filed|petition|preparing))",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "fv_screening_outcome": {
        "label": "Family violence screening outcome (presence)",
        "patterns": [r"(family\s+violence[^\n]{0,200}(?:no|none|not\s+applicable|not\s+raised|screening))"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "orders_sought": {
        "label": "Orders sought (presence)",
        "patterns": [r"(?:^|\n)\s*(?:Order\s+)?(\d+\.\s+(?:That|The))"],
        "norm": lambda s: "PRESENT" if s else "",
        "multi": True,
    },
    "case_number_assigned": {
        "label": "FCFCOA case number once filed",
        "patterns": [
            r"\b((?:SYC|MEL|BRC)\s?\d{2,}\s?(?:/\s?\d{4})?)",
        ],
        "norm": _norm_id,
    },
    "income_history_5yr": {
        "label": "5+ years of ATI history (presence)",
        "patterns": [
            r"(2018[-–]19|2020[-–]21|2021[-–]22|2022[-–]23|2023[-–]24)[^\n]{0,80}\$\s*([0-9,]+)",
        ],
        "norm": lambda s: "PRESENT" if s else "",
        "multi": True,
    },
    "workers_comp_status": {
        "label": "Workers compensation current-status flag",
        "patterns": [
            r"(workers?\s+comp(?:ensation)?[^\n]{0,80}(?:since|from|January\s+2024))",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "asset_pool_overview": {
        "label": "Asset pool overview (presence)",
        "patterns": [
            r"(?:asset(?:s)?(?:\s+pool)?\s+(?:overview|summary|list|schedule)|assets\s+(?:are|comprise|include))",
        ],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "tempe_sale_disposition": {
        "label": "Disposition of Tempe sale (presence)",
        "patterns": [r"(Tempe[^\n]{0,200}(?:sold|disposed|proceeds|net))"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "income_other_years_summary": {
        "label": "Income history other years (presence)",
        "patterns": [r"(2018[-–]19|2020[-–]21|2021[-–]22|2022[-–]23|2023[-–]24)"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "income_total_weekly_gross": {
        "label": "Total weekly gross income",
        "patterns": [
            r"(?:total|gross)\s+(?:weekly\s+)?income[^\n]{0,80}?\$\s*([0-9,]+)",
        ],
        "norm": _norm_dollar,
    },
    "income_total_weekly_net": {
        "label": "Total weekly net income",
        "patterns": [
            r"net\s+(?:weekly\s+)?income[^\n]{0,80}?\$\s*([0-9,]+)",
        ],
        "norm": _norm_dollar,
    },
    "asset_pool_total": {
        "label": "Total asset pool",
        "patterns": [
            r"total\s+assets?[^\n]{0,80}?\$\s*([0-9,]+)",
        ],
        "norm": _norm_dollar,
    },
    "liability_pool_total": {
        "label": "Total liabilities",
        "patterns": [
            r"total\s+liabilit(?:ies|y)[^\n]{0,80}?\$\s*([0-9,]+)",
        ],
        "norm": _norm_dollar,
    },
    "creditors_list": {
        "label": "Creditors list (presence)",
        "patterns": [r"(creditors?\s+(?:list|schedule)|secured\s+(?:and\s+unsecured\s+)?creditors)"],
        "norm": lambda s: "PRESENT" if s else "",
    },
    "service_method": {
        "label": "DPO service method on Peter",
        "patterns": [
            r"(?:served|service)[^\n]{0,200}?(post|email|hand|in\s+person|registered)",
        ],
        "norm": _norm_text,
    },
    "dpo_delegate": {
        "label": "Name of SA delegate who issued DPO (presence)",
        "patterns": [r"(delegate\s+of\s+the\s+Registrar|by\s+its\s+delegate)"],
        "norm": lambda s: "PRESENT" if s else "",
    },
}


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_docs(matter_root: Path) -> dict:
    """Return {doc_id: Path or None}."""
    found = {}
    for d in DOCS:
        path = None
        for pattern in d["discovery_patterns"]:
            for p in matter_root.glob(pattern):
                if p.is_file():
                    path = p
                    break
            if path:
                break
        found[d["id"]] = path
    return found


# ---------------------------------------------------------------------------
# Extraction per doc
# ---------------------------------------------------------------------------

def extract_field(text: str, field_id: str) -> list[str]:
    spec = FIELD_EXTRACTORS.get(field_id)
    if not spec:
        return []
    values: list[str] = []
    seen = set()
    for pattern in spec["patterns"]:
        for m in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            try:
                raw = m.group(1)
            except IndexError:
                raw = m.group(0)
            if raw is None:
                continue
            normed = spec["norm"](raw)
            if not normed:
                continue
            if normed not in seen:
                seen.add(normed)
                values.append(normed)
        if values and not spec.get("multi"):
            break
    return values


def extract_doc(path: Path, expected: list[str]) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: dict = {}
    for field in expected:
        out[field] = extract_field(text, field)
    return out


# ---------------------------------------------------------------------------
# Cross-doc analysis
# ---------------------------------------------------------------------------

def cross_doc_analyse(extracted: dict) -> dict:
    """For each field that appears in 2+ docs, check consistency."""
    by_field: dict[str, dict[str, list[str]]] = defaultdict(dict)
    for doc_id, fields in extracted.items():
        for field, values in fields.items():
            if values:
                by_field[field][doc_id] = values

    analysis = {"consistent": [], "drift": [], "single_source": [], "absent": []}

    all_field_ids = set()
    for d in DOCS:
        all_field_ids.update(d["expected_fields"])

    for field in sorted(all_field_ids):
        spec = FIELD_EXTRACTORS.get(field)
        if not spec:
            continue
        sources = by_field.get(field, {})
        if not sources:
            analysis["absent"].append(field)
        elif len(sources) == 1:
            analysis["single_source"].append((field, sources))
        else:
            # 2+ sources — compare canonical values
            # For multi-value fields (lists), compare as SORTED SET (order doesn't matter)
            # For party names + free text fields, case-fold for comparison too
            is_multi = bool(spec.get("multi"))
            normaliser = (lambda v: v.casefold()) if field in {
                "peter_full_name", "sarah_full_name",
            } else (lambda v: v)
            per_doc_canonical: dict[str, frozenset[str]] = {}
            for doc_id, vs in sources.items():
                per_doc_canonical[doc_id] = frozenset(normaliser(v) for v in vs)
            distinct_canonicals = set(per_doc_canonical.values())
            if len(distinct_canonicals) == 1:
                # Pick a display value from the first doc
                display = ", ".join(sorted(sources[list(sources.keys())[0]])) if is_multi else list(sources.values())[0][0]
                analysis["consistent"].append((field, sources, display))
            else:
                all_values = set()
                for vs in sources.values():
                    for v in vs:
                        all_values.add(v)
                analysis["drift"].append((field, sources, all_values))

    return analysis


# ---------------------------------------------------------------------------
# Gap analysis per doc
# ---------------------------------------------------------------------------

def gap_analysis(found: dict, extracted: dict) -> dict:
    """For each doc that exists, list expected fields that weren't found."""
    gaps = {}
    for d in DOCS:
        doc_id = d["id"]
        if not found.get(doc_id):
            continue
        doc_extract = extracted.get(doc_id, {})
        missing = [f for f in d["expected_fields"] if not doc_extract.get(f)]
        gaps[doc_id] = missing
    return gaps


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def render(matter_root: Path, found: dict, extracted: dict, analysis: dict, gaps: dict) -> str:
    today = date.today().isoformat()
    parts: list[str] = []
    parts.append(f"# Metis — 4-Document Consistency Reconciliation Report\n\n")
    parts.append(f"**Matter:** `{matter_root}`\n")
    parts.append(f"**Generated:** {today}\n")
    parts.append(f"**Documents tracked:** {len(DOCS)}\n\n")
    parts.append(
        "Tracks factual disclosure across the four documents that must tell **one consistent story** "
        "across Peter's parallel proceedings:\n\n"
    )
    for d in DOCS:
        path = found.get(d["id"])
        marker = "✅ found" if path else "❌ not yet drafted"
        rel = path.relative_to(matter_root).as_posix() if path else "—"
        parts.append(f"- **{d['label']}** — {marker} · `{rel}`\n")
    parts.append("\n---\n\n")

    # SUMMARY
    parts.append("## Summary at a glance\n\n")
    parts.append(f"- ✅ **Consistent across docs:** {len(analysis['consistent'])} field(s)\n")
    parts.append(f"- ⚠️ **Drift detected (values differ):** {len(analysis['drift'])} field(s)\n")
    parts.append(f"- 🔍 **Single-source (only one doc has it):** {len(analysis['single_source'])} field(s)\n")
    parts.append(f"- 🕳️ **Absent (not yet captured anywhere):** {len(analysis['absent'])} field(s)\n\n")

    # DRIFT FLAGS — highest priority
    if analysis["drift"]:
        parts.append("## ⚠️ Drift flags — these MUST be reconciled before any filing\n\n")
        for field, sources, all_values in analysis["drift"]:
            spec = FIELD_EXTRACTORS.get(field, {})
            label = spec.get("label", field)
            parts.append(f"### {label}  (`{field}`)\n\n")
            parts.append(f"Different values found across {len(sources)} docs:\n\n")
            for doc_id, values in sources.items():
                parts.append(f"- **{_doc_label(doc_id)}:** {', '.join(f'`{v}`' for v in values)}\n")
            parts.append("\n")
        parts.append("---\n\n")

    # CONSISTENT — confirm load-bearing claims
    if analysis["consistent"]:
        parts.append("## ✅ Consistent across docs (load-bearing claims — protect these)\n\n")
        parts.append("| Field | Value | In docs |\n|---|---|---|\n")
        for field, sources, value in analysis["consistent"]:
            spec = FIELD_EXTRACTORS.get(field, {})
            label = spec.get("label", field)
            docs_str = ", ".join(_doc_label(d) for d in sources.keys())
            parts.append(f"| {label} | `{value}` | {docs_str} |\n")
        parts.append("\n---\n\n")

    # SINGLE-SOURCE — needs cross-referencing
    if analysis["single_source"]:
        parts.append("## 🔍 Single-source (only in one doc — consider whether others need it)\n\n")
        parts.append("| Field | Value | Only in | Other docs that should probably have it |\n|---|---|---|---|\n")
        for field, sources in analysis["single_source"]:
            spec = FIELD_EXTRACTORS.get(field, {})
            label = spec.get("label", field)
            doc_id, values = list(sources.items())[0]
            vals_str = ", ".join(f"`{v}`" for v in values)
            # Which other docs expect this field?
            other_docs = [d["label"] for d in DOCS if field in d["expected_fields"] and d["id"] != doc_id]
            others_str = "; ".join(other_docs) if other_docs else "—"
            parts.append(f"| {label} | {vals_str} | {_doc_label(doc_id)} | {others_str} |\n")
        parts.append("\n---\n\n")

    # PER-DOC GAP ANALYSIS
    parts.append("## 🕳️ Per-doc gap analysis\n\n")
    for d in DOCS:
        doc_id = d["id"]
        if not found.get(doc_id):
            parts.append(f"### {d['label']} — *not yet drafted*\n\n")
            parts.append(f"All {len(d['expected_fields'])} expected fields will need capture once drafting begins:\n\n")
            for f in d["expected_fields"]:
                lbl = FIELD_EXTRACTORS.get(f, {}).get("label", f)
                parts.append(f"- {lbl}\n")
            parts.append("\n")
            continue
        missing = gaps.get(doc_id, [])
        present = [f for f in d["expected_fields"] if f not in missing]
        parts.append(f"### {d['label']} — {len(present)}/{len(d['expected_fields'])} expected fields present\n\n")
        if missing:
            parts.append(f"**Missing from this doc (consider whether they belong here):**\n\n")
            for f in missing:
                lbl = FIELD_EXTRACTORS.get(f, {}).get("label", f)
                parts.append(f"- {lbl}\n")
            parts.append("\n")
        else:
            parts.append("All expected fields captured.\n\n")

    # ABSENT — fields nobody has captured anywhere
    if analysis["absent"]:
        parts.append("## ❌ Absent from all docs (not yet captured anywhere)\n\n")
        for f in sorted(analysis["absent"]):
            lbl = FIELD_EXTRACTORS.get(f, {}).get("label", f)
            relevant_docs = [d["label"] for d in DOCS if f in d["expected_fields"]]
            parts.append(f"- **{lbl}** — relevant to: {'; '.join(relevant_docs)}\n")
        parts.append("\n")

    # Reading guide
    parts.append("---\n\n## Reading this report\n\n")
    parts.append(
        "1. **Drift flags first** — these are the inconsistencies that cause credibility damage. "
        "Pick the correct value and propagate it everywhere it should appear.\n\n"
        "2. **Single-source fields** — review whether the value should propagate to other docs. "
        "Sometimes it should (CRN, party identifiers); sometimes a fact belongs only in one doc (case "
        "number is only in the Initiating Application).\n\n"
        "3. **Per-doc gaps** — for each existing doc, what's missing that should be there?\n\n"
        "4. **Absent fields** — facts nobody has captured yet. As each doc gets drafted, this list shrinks.\n\n"
        "5. **Re-run after every material edit.** Pattern-based, deterministic, <1 second. "
        "Honest pre-filing sanity check.\n\n"
    )
    parts.append("---\n\n")
    parts.append(
        "*Prototype #4 of the Metis client-side build — 4-Doc Consistency Reconciliation. "
        "Pattern-based; LLM enrichment for paraphrase detection deferred to Phase 1 build. "
        "Source: `~/Desktop/metis-cortex/prototypes/four_doc_check.py`.*\n"
    )

    return "".join(parts)


def _doc_label(doc_id: str) -> str:
    for d in DOCS:
        if d["id"] == doc_id:
            return d["label"]
    return doc_id


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    matter = (
        Path(sys.argv[1]).expanduser().resolve()
        if len(sys.argv) >= 2
        else Path.home() / "Desktop/child-support-stay-order"
    )
    if not matter.is_dir():
        print(f"matter folder not found: {matter}", file=sys.stderr)
        return 2

    output = (
        Path(sys.argv[2]).expanduser().resolve()
        if len(sys.argv) >= 3
        else Path.home() / "Desktop/metis-cortex" / f"RECONCILIATION-REPORT-{date.today().isoformat()}.md"
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    found = discover_docs(matter)
    extracted: dict = {}
    for d in DOCS:
        doc_id = d["id"]
        path = found.get(doc_id)
        if path:
            extracted[doc_id] = extract_doc(path, d["expected_fields"])
        else:
            extracted[doc_id] = {}

    analysis = cross_doc_analyse(extracted)
    gaps = gap_analysis(found, extracted)
    report = render(matter, found, extracted, analysis, gaps)
    output.write_text(report, encoding="utf-8")

    print(f"matter: {matter}")
    print(f"docs found: {sum(1 for p in found.values() if p)}/{len(DOCS)}")
    print(f"drift flags: {len(analysis['drift'])}")
    print(f"consistent fields: {len(analysis['consistent'])}")
    print(f"single-source: {len(analysis['single_source'])}")
    print(f"absent: {len(analysis['absent'])}")
    print(f"report: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
