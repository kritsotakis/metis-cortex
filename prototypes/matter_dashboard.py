#!/usr/bin/env python3
"""
Metis — Matter Dashboard (Prototype #2)

Reads an on-disk matter folder and generates a single self-contained HTML
page summarising the matter state: parallel streams, outstanding work,
recent activity, deadlines, key drafts.

The HTML is renderable without a server. Open it in any browser. Bookmark it.
Re-run after each material change in the matter; the file regenerates in <1s.

Design:
  - Pattern-based, deterministic (same input → same output)
  - Self-contained (no external CSS / JS / fonts)
  - On-brand (navy/gold/cream, Playfair Display fallback to system serif)
  - Mobile-friendly (single-column on narrow viewports)
  - Read-only against the matter folder

Usage:
  python3 matter_dashboard.py [matter_folder] [output_html]

Defaults:
  matter_folder = ~/Desktop/child-support-stay-order
  output_html   = ~/Desktop/metis-cortex/dashboard.html
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date, datetime
from html import escape
from pathlib import Path

# ---------------------------------------------------------------------------
# Brand tokens
# ---------------------------------------------------------------------------

NAVY = "#0f1e3d"
NAVY_DEEP = "#0b1730"
GOLD = "#c9a84c"
GOLD_DARK = "#9a7d2e"
CREAM = "#f5f0e8"
INK = "#1a2438"
TEXT_DIM = "#1a2438cc"
TEXT_FAINT = "#1a243899"


# ---------------------------------------------------------------------------
# Matter-specific knowledge — for the DPO matter today, parameterised tomorrow
# ---------------------------------------------------------------------------
#
# This is the matter brain: the structure that the dashboard renders against.
# Each entry is keyed by stream id so we can detect updates in the on-disk
# files and reflect them. For a generic matter the dashboard would read this
# from a matter.yaml in the folder; for the DPO matter we embed it inline.

STREAMS = [
    {
        "id": "fcfcoa",
        "name": "FCFCOA stay + s.112 leave",
        "decision_maker": "Federal Circuit and Family Court (Sydney Registry)",
        "deadline_iso": None,
        "deadline_text": "Self-imposed ASAP (DPO blocking overseas travel)",
        "key_drafts": [
            "drafts/01_initiating_application_CONTENT.md",
            "drafts/02_affidavit.md",
            "drafts/04_cover_letter_urgency.md",
        ],
        "status_summary": "Drafts current; 6 REDLINE items gating witnessing",
    },
    {
        "id": "sa_coa_response",
        "name": "Response to Sarah's Reason 8B Change of Assessment",
        "decision_maker": "Services Australia (Child Support)",
        "deadline_iso": "2026-06-15",
        "deadline_text": "15 June 2026 (hard)",
        "key_drafts": [
            "drafts/06_sa_response_to_sarah_coa_2026-06-15.md",
            "prior-application/sa_sarah_coa_application_2026-06-01.md",
        ],
        "status_summary": "Sarah filed 1 June 2026 (Reason 8B — earning capacity). Response due 15 Jun (14 days). Disclosure must be consistent across 4 docs (this response + FCFCOA affidavit + FCFCOA Financial Statement + bankruptcy SoA). Requires 6mo bank statements + Workcover + P&L/BS/depn for current + last 2 FY.",
    },
    {
        "id": "bankruptcy",
        "name": "Bankruptcy petition (debtor's)",
        "decision_maker": "AFSA",
        "deadline_iso": None,
        "deadline_text": "A couple of months away",
        "key_drafts": [
            "drafts/05_email_alice_russell_bankruptcy_transfer.md",
        ],
        "status_summary": "Statement of Affairs in preparation by Alice Russell (Wesley)",
    },
    {
        "id": "dpo_admin",
        "name": "DPO admin — copy request + revocation",
        "decision_maker": "Services Australia (Child Support Registrar)",
        "deadline_iso": None,
        "deadline_text": "Concurrent with FCFCOA filing",
        "key_drafts": [
            "drafts/06_sa_dpo_copy_request.md",
            "drafts/07_sa_foi_dpo_request.md",
        ],
        "status_summary": "Admin request letter ready; FOI fallback ready if SA non-responsive in 14 days",
    },
]


REDLINE_ITEMS = [
    {
        "id": "F4",
        "para": "Initiating App — Order 3",
        "summary": "$50/week floor reads as contempt",
        "status": "DONE — $50 floor removed; Orders 1–7 restructured per s.112 reframe",
        "severity": "done",
        "gating": False,
        "input_from": "—",
    },
    {
        "id": "F14",
        "para": "Affidavit Para 16",
        "summary": "Jurisdictional premise — Option A applies",
        "status": "UNBLOCKED — 1 July 2025 SA rejection letter received 29 May 2026; Para 16 cites the real letter",
        "severity": "unblocked",
        "gating": False,
        "input_from": "—",
    },
    {
        "id": "F15",
        "para": "Affidavit Para 17",
        "summary": "DPO referenced and now sighted",
        "status": "UNBLOCKED — 23 Dec 2024 DPO notice received 29 May 2026; Para 17 cites the real letter",
        "severity": "unblocked",
        "gating": False,
        "input_from": "—",
    },
    {
        "id": "F16",
        "para": "Affidavit Paras 19 + 24(a)",
        "summary": "DSK income compliance statement (self-incrimination risk)",
        "status": "GATING — needs ATO lodgement BEFORE swearing",
        "severity": "critical",
        "gating": True,
        "input_from": "Peter lodges DSK with ATO (BAS or income disclosure) → date + confirmation PDF for Annexure K",
    },
    {
        "id": "E7",
        "para": "Affidavit Para 23C (NEW)",
        "summary": "Kritsotakis Family Trust + Pty Ltd disclosure",
        "status": "GATING — framing locked; ASIC extract needed for Annexure L",
        "severity": "critical",
        "gating": True,
        "input_from": "Peter does paid ASIC Connect extract for Kritsotakis Investments Pty Ltd",
    },
    {
        "id": "F8",
        "para": "Affidavit Para 23B v3",
        "summary": "Tempe net proceeds dollar breakdown (~$1.28M sale)",
        "status": "GATING — Wesley email ready (draft 08, needs DPO-side review); template populates from his reply",
        "severity": "high",
        "gating": True,
        "input_from": "Wesley (accountant) reply with mortgage + commission + Sarah + FTX + FX + residual figures",
    },
]


# ---------------------------------------------------------------------------
# PAIR.md parsing — pull state from the auto-header + recent entries
# ---------------------------------------------------------------------------

def parse_pair_header(text: str) -> dict:
    """Pull the auto-rendered header block from PAIR.md."""
    out = {
        "owner_now": "",
        "peter_blocked": "",
        "waiting_cowork": "",
        "waiting_code": "",
        "stale": "",
        "last_touched": "",
        "total_entries": "",
        "action_queue": [],
    }
    header_match = re.search(
        r"<!-- AUTO-HEADER.*?-->\s*\n(.*?)\n<!-- /AUTO-HEADER -->",
        text,
        re.DOTALL,
    )
    if not header_match:
        return out
    header = header_match.group(1)
    for key, pattern in [
        ("owner_now", r"\*\*Owner now\*\*\s*\|\s*(.+?)\s*\|"),
        ("peter_blocked", r"\*\*🔴 Peter blocked\*\*\s*\|\s*(.+?)\s*\|"),
        ("waiting_cowork", r"\*\*⏸️ Waiting on cowork\*\*\s*\|\s*(.+?)\s*\|"),
        ("waiting_code", r"\*\*⏸️ Waiting on code\*\*\s*\|\s*(.+?)\s*\|"),
        ("stale", r"\*\*Stale \(>SLA\)\*\*\s*\|\s*(.+?)\s*\|"),
        ("last_touched", r"\*\*Last touched\*\*\s*\|\s*(.+?)\s*\|"),
        ("total_entries", r"\*\*Total entries\*\*\s*\|\s*(.+?)\s*\|"),
    ]:
        m = re.search(pattern, header)
        if m:
            out[key] = m.group(1).strip()
    # Action queue items
    queue_match = re.search(r"\*\*Action queue.*?\*\*[:\s]*\n(.*?)(?:\n\n|\Z)", header, re.DOTALL)
    if queue_match:
        for line in queue_match.group(1).splitlines():
            line = line.strip()
            if line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "-")):
                # Strip leading numbering + bullets, then strip markdown emphasis
                cleaned = re.sub(r"^[\d\.\-\s]+", "", line).strip()
                cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", cleaned)  # bold → plain
                cleaned = re.sub(r"\*([^*]+)\*", r"\1", cleaned)  # italic → plain
                cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)  # inline code → plain
                if cleaned and "empty" not in cleaned.lower():
                    out["action_queue"].append(cleaned)
    return out


def derive_last_touched(matter_root: Path, pair_text: str, header_value: str) -> str:
    """Use the fresher of: PAIR.md file mtime vs the auto-header value.

    Bug surfaced by the DPO session 2026-06-01: the auto-header value is only
    fresh when pair-render.py has been re-run, which doesn't happen on every
    PAIR.md edit. The file mtime is the ground truth.
    """
    pair_path = matter_root / "PAIR.md"
    if not pair_path.is_file():
        return header_value or "—"
    mtime = datetime.fromtimestamp(pair_path.stat().st_mtime)
    mtime_str = mtime.strftime("%Y-%m-%d %H:%M")
    # Try to parse the header value to a datetime for comparison
    if header_value:
        # Header format observed: "2026-06-01 00:00 AEST · code"
        m = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{2})", header_value)
        if m:
            try:
                header_dt = datetime.strptime(f"{m.group(1)} {m.group(2)}", "%Y-%m-%d %H:%M")
                if mtime > header_dt:
                    return f"{mtime_str} (file mtime; auto-header is stale: {header_value})"
                return header_value
            except ValueError:
                pass
    return f"{mtime_str} (file mtime)"


def parse_pair_entries(text: str, n: int = 5) -> list[dict]:
    """Extract the last N entries from PAIR.md."""
    entries = []
    # PAIR entries are headed by ### YYYY-MM-DD ...
    pattern = re.compile(
        r"### (\d{4}-\d{2}-\d{2}[^\n]*?)\n(.*?)(?=\n### |\Z)",
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        header = m.group(1).strip()
        body = m.group(2).strip()
        # First "Did:" line
        did_match = re.search(r"\*\*Did:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)", body)
        status_match = re.search(r"\*\*Status:\*\*\s*([^\n]+)", body)
        entries.append({
            "header": header,
            "did": (did_match.group(1).strip().replace("\n", " ") if did_match else "")[:280],
            "status": status_match.group(1).strip() if status_match else "",
        })
    # Return the last N (most recent are usually at the bottom of the file)
    return entries[-n:][::-1]  # reverse so newest first


# ---------------------------------------------------------------------------
# Folder scan — count files in key folders
# ---------------------------------------------------------------------------

def folder_stats(root: Path) -> dict:
    stats = {}
    for sub in ["drafts", "prior-application", "annexures", "filing", "filled", "forms", "reference", "factsheets"]:
        p = root / sub
        if p.is_dir():
            files = [f for f in p.iterdir() if f.is_file() and not f.name.startswith(".")]
            stats[sub] = {"count": len(files), "exists": True}
        else:
            stats[sub] = {"count": 0, "exists": False}
    return stats


def list_drafts(root: Path) -> list[dict]:
    drafts_dir = root / "drafts"
    if not drafts_dir.is_dir():
        return []
    out = []
    for f in sorted(drafts_dir.iterdir()):
        if f.is_file() and f.suffix == ".md" and not f.name.startswith("."):
            stat = f.stat()
            out.append({
                "name": f.name,
                "size_kb": round(stat.st_size / 1024, 1),
                "mtime": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "rel_path": f"drafts/{f.name}",
            })
    return out


def days_until(iso_date: str | None) -> int | None:
    if not iso_date:
        return None
    try:
        d = datetime.strptime(iso_date, "%Y-%m-%d").date()
    except ValueError:
        return None
    return (d - date.today()).days


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def render_html(matter_root: Path, header: dict, entries: list[dict], stats: dict, drafts: list[dict]) -> str:
    matter_name = matter_root.name.replace("-", " ").title()
    now = datetime.now().strftime("%a %d %b %Y · %H:%M")

    # Stream rendering
    streams_html = ""
    for s in STREAMS:
        days = days_until(s["deadline_iso"])
        deadline_class = "deadline-soon" if (days is not None and days <= 21) else ""
        days_str = ""
        if days is not None:
            if days < 0:
                days_str = f'<span class="days-flag overdue">{-days} days overdue</span>'
            elif days <= 14:
                days_str = f'<span class="days-flag soon">{days} days</span>'
            else:
                days_str = f'<span class="days-flag normal">{days} days</span>'
        drafts_list = "".join(
            f'<li><code>{escape(d)}</code></li>'
            for d in s["key_drafts"]
        )
        streams_html += f'''
        <div class="stream">
          <div class="stream-head">
            <div class="stream-name">{escape(s["name"])}</div>
            <div class="stream-meta">
              <span class="meta-label">Decided by</span> {escape(s["decision_maker"])}
              <span class="meta-sep">·</span>
              <span class="meta-label">Deadline</span> <span class="{deadline_class}">{escape(s["deadline_text"])}</span>
              {days_str}
            </div>
          </div>
          <div class="stream-status">{escape(s["status_summary"])}</div>
          <ul class="drafts-list">{drafts_list}</ul>
        </div>
        '''

    # Redline rendering — severity badges + gating flags + status text per item
    redline_html = ""
    severity_labels = {
        "critical": ("CRITICAL", "🔴"),
        "high": ("HIGH", "🟠"),
        "done": ("DONE", "✅"),
        "unblocked": ("UNBLOCKED", "✅"),
        "low": ("LOW", "⚪"),
    }
    for r in REDLINE_ITEMS:
        sev_class = f"sev-{r['severity']}"
        sev_label, sev_icon = severity_labels.get(r["severity"], ("?", "·"))
        sev_badge = f'<span class="sev-badge sev-badge-{r["severity"]}">{sev_icon} {sev_label}</span>'
        gating_label = '<span class="gating-flag">GATING</span>' if r["gating"] else ""
        redline_html += f'''
        <tr class="{sev_class}">
          <td class="redline-id">{escape(r["id"])} {sev_badge} {gating_label}</td>
          <td class="redline-para">{escape(r["para"])}</td>
          <td class="redline-summary">{escape(r["summary"])}</td>
          <td class="redline-status">{escape(r["status"])}</td>
          <td class="redline-input">{escape(r["input_from"])}</td>
        </tr>
        '''

    # Drafts table
    drafts_html = "".join(
        f'<tr><td class="d-name">{escape(d["name"])}</td>'
        f'<td class="d-size">{d["size_kb"]} KB</td>'
        f'<td class="d-mtime">{escape(d["mtime"])}</td></tr>'
        for d in drafts
    )

    # Recent activity
    entries_html = ""
    for e in entries:
        status_html = f'<span class="entry-status">{escape(e["status"])}</span>' if e["status"] else ""
        entries_html += f'''
        <div class="entry">
          <div class="entry-head"><span class="entry-when">{escape(e["header"])}</span>{status_html}</div>
          <div class="entry-did">{escape(e["did"])}</div>
        </div>
        '''

    # Action queue
    action_html = ""
    if header["action_queue"]:
        action_html = '<ul class="action-queue">' + "".join(
            f"<li>{escape(a)}</li>" for a in header["action_queue"]
        ) + "</ul>"
    else:
        action_html = '<p class="action-empty">Action queue empty — both sides caught up.</p>'

    # Folder stats
    stats_html = ""
    for k, v in stats.items():
        if v["exists"]:
            stats_html += f'<div class="stat-item"><span class="stat-label">{escape(k)}/</span><span class="stat-val">{v["count"]}</span></div>'

    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Metis — {escape(matter_name)} Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; padding: 0; background: {CREAM}; color: {INK};
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 15px; line-height: 1.55;
    }}
    .container {{ max-width: 1100px; margin: 0 auto; padding: 2rem 1.5rem; }}
    h1, h2, h3 {{ font-family: 'Playfair Display', Georgia, serif; font-weight: 600; color: {NAVY}; margin: 0; }}
    h1 {{ font-size: 2.2rem; line-height: 1.1; }}
    h2 {{ font-size: 1.5rem; margin: 2.5rem 0 1rem; }}
    h3 {{ font-size: 1.1rem; margin: 1.5rem 0 0.5rem; }}
    .gold-rule {{ display: block; width: 3rem; height: 2px; background: {GOLD}; margin: 0 0 1rem; }}
    .eyebrow {{ text-transform: uppercase; letter-spacing: 0.18em; color: {GOLD_DARK}; font-weight: 600; font-size: 0.7rem; margin-bottom: 0.5rem; }}

    /* Top bar */
    .topbar {{
      background: {NAVY}; color: {CREAM};
      padding: 1.5rem 0;
    }}
    .topbar h1 {{ color: {CREAM}; }}
    .topbar .container {{ padding-top: 0; padding-bottom: 0; }}
    .topbar-meta {{ color: rgba(245,240,232,0.7); font-size: 0.85rem; margin-top: 0.3rem; }}

    /* Status snapshot */
    .status-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 0.75rem; margin-bottom: 1.5rem;
    }}
    .stat-card {{
      background: white; border: 1px solid rgba(15,30,61,0.08);
      border-radius: 8px; padding: 0.9rem 1rem;
      box-shadow: 0 1px 2px rgba(15,30,61,0.04);
    }}
    .stat-card .label {{ font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; color: {GOLD_DARK}; font-weight: 600; }}
    .stat-card .value {{ font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; color: {NAVY}; margin-top: 0.2rem; }}
    .stat-card.alert {{ border-left: 3px solid #d73a49; }}
    .stat-card.alert .value {{ color: #d73a49; }}

    /* Action queue */
    .action-queue {{ list-style: none; padding: 0; margin: 0; }}
    .action-queue li {{
      background: white; border: 1px solid rgba(15,30,61,0.08);
      border-left: 3px solid {GOLD};
      padding: 0.7rem 1rem; margin-bottom: 0.4rem; border-radius: 6px;
      font-size: 0.92rem;
    }}
    .action-empty {{ color: {TEXT_FAINT}; font-style: italic; }}

    /* Streams */
    .stream {{
      background: white; border: 1px solid rgba(15,30,61,0.08);
      border-radius: 8px; padding: 1rem 1.2rem; margin-bottom: 0.8rem;
      box-shadow: 0 1px 2px rgba(15,30,61,0.04);
    }}
    .stream-head {{ display: flex; flex-direction: column; gap: 0.3rem; margin-bottom: 0.5rem; }}
    .stream-name {{ font-family: 'Playfair Display', Georgia, serif; font-size: 1.15rem; color: {NAVY}; font-weight: 600; }}
    .stream-meta {{ font-size: 0.82rem; color: {TEXT_DIM}; }}
    .meta-label {{ color: {GOLD_DARK}; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.7rem; font-weight: 600; margin-right: 0.3rem; }}
    .meta-sep {{ margin: 0 0.5rem; color: rgba(26,36,56,0.3); }}
    .days-flag {{ display: inline-block; padding: 0.1rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; margin-left: 0.4rem; }}
    .days-flag.overdue {{ background: #d73a49; color: white; }}
    .days-flag.soon {{ background: rgba(255,170,40,0.18); color: #b67500; }}
    .days-flag.normal {{ background: rgba(15,30,61,0.06); color: {NAVY}; }}
    .deadline-soon {{ color: #b67500; font-weight: 600; }}
    .stream-status {{ font-size: 0.92rem; color: {INK}; margin-bottom: 0.5rem; }}
    .drafts-list {{ list-style: none; padding: 0; margin: 0; }}
    .drafts-list li {{ display: inline-block; margin: 0.15rem 0.4rem 0.15rem 0; font-size: 0.78rem; }}
    .drafts-list code {{ background: rgba(15,30,61,0.05); padding: 0.15rem 0.45rem; border-radius: 4px; color: {NAVY}; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}

    /* Redline table */
    .redline-table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 2px rgba(15,30,61,0.04); border: 1px solid rgba(15,30,61,0.08); }}
    .redline-table th {{ text-align: left; padding: 0.7rem 0.9rem; background: {NAVY}; color: {CREAM}; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }}
    .redline-table td {{ padding: 0.7rem 0.9rem; vertical-align: top; font-size: 0.88rem; border-top: 1px solid rgba(15,30,61,0.06); }}
    .redline-id {{ font-weight: 600; color: {NAVY}; white-space: nowrap; }}
    .gating-flag {{ display: inline-block; background: rgba(215,58,73,0.12); color: #d73a49; padding: 0.05rem 0.4rem; border-radius: 3px; font-size: 0.65rem; font-weight: 700; letter-spacing: 0.06em; margin-left: 0.3rem; }}
    .sev-badge {{ display: inline-block; padding: 0.05rem 0.4rem; border-radius: 3px; font-size: 0.65rem; font-weight: 700; letter-spacing: 0.06em; margin-left: 0.3rem; }}
    .sev-badge-critical {{ background: rgba(215,58,73,0.15); color: #d73a49; }}
    .sev-badge-high {{ background: rgba(201,168,76,0.18); color: {GOLD_DARK}; }}
    .sev-badge-done {{ background: rgba(40,167,69,0.15); color: #1e7a32; }}
    .sev-badge-unblocked {{ background: rgba(40,167,69,0.15); color: #1e7a32; }}
    .sev-badge-low {{ background: rgba(15,30,61,0.08); color: {NAVY}; }}
    .sev-critical td:first-child {{ border-left: 3px solid #d73a49; }}
    .sev-high td:first-child {{ border-left: 3px solid {GOLD}; }}
    .sev-done td:first-child {{ border-left: 3px solid #1e7a32; }}
    .sev-unblocked td:first-child {{ border-left: 3px solid #1e7a32; }}
    .sev-done td, .sev-unblocked td {{ color: {TEXT_DIM}; }}

    /* Drafts table */
    .drafts-table {{ width: 100%; border-collapse: collapse; background: white; border: 1px solid rgba(15,30,61,0.08); border-radius: 8px; overflow: hidden; }}
    .drafts-table th {{ background: rgba(15,30,61,0.04); padding: 0.6rem 0.9rem; text-align: left; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: {GOLD_DARK}; font-weight: 600; }}
    .drafts-table td {{ padding: 0.55rem 0.9rem; font-size: 0.85rem; border-top: 1px solid rgba(15,30,61,0.06); font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
    .d-name {{ color: {NAVY}; font-weight: 500; }}
    .d-size, .d-mtime {{ color: {TEXT_DIM}; }}

    /* Recent activity */
    .entry {{
      background: white; border: 1px solid rgba(15,30,61,0.08); border-radius: 6px;
      padding: 0.8rem 1rem; margin-bottom: 0.4rem;
    }}
    .entry-head {{ display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; }}
    .entry-when {{ font-weight: 600; color: {NAVY}; font-size: 0.85rem; }}
    .entry-status {{ font-size: 0.78rem; color: {GOLD_DARK}; }}
    .entry-did {{ color: {TEXT_DIM}; font-size: 0.85rem; margin-top: 0.3rem; }}

    /* Folder stats */
    .folder-stats {{ display: flex; gap: 0.8rem; flex-wrap: wrap; margin-top: 1rem; }}
    .stat-item {{ background: white; border: 1px solid rgba(15,30,61,0.08); border-radius: 6px; padding: 0.5rem 0.8rem; font-size: 0.85rem; }}
    .stat-label {{ color: {TEXT_DIM}; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; margin-right: 0.4rem; }}
    .stat-val {{ font-weight: 600; color: {NAVY}; }}

    /* Footer */
    footer {{ background: {NAVY_DEEP}; color: rgba(245,240,232,0.6); padding: 1.5rem 0; font-size: 0.78rem; margin-top: 3rem; }}
    footer a {{ color: {GOLD}; text-decoration: none; }}
  </style>
</head>
<body>

<div class="topbar">
  <div class="container">
    <h1>Metis · {escape(matter_name)}</h1>
    <div class="topbar-meta">Generated {escape(now)} · <code style="color:rgba(245,240,232,0.6);">{escape(str(matter_root))}</code></div>
  </div>
</div>

<div class="container">

  <!-- STATUS SNAPSHOT -->
  <span class="gold-rule"></span>
  <p class="eyebrow">Status snapshot · from PAIR.md auto-header</p>
  <h2>Where the matter is right now</h2>
  <div class="status-grid">
    <div class="stat-card"><div class="label">Owner now</div><div class="value">{escape(header["owner_now"] or "—")}</div></div>
    <div class="stat-card{' alert' if header["peter_blocked"] and header["peter_blocked"] != "none" else ''}"><div class="label">🔴 Peter blocked</div><div class="value">{escape(header["peter_blocked"] or "—")}</div></div>
    <div class="stat-card"><div class="label">⏸️ Waiting cowork</div><div class="value">{escape(header["waiting_cowork"] or "—")}</div></div>
    <div class="stat-card"><div class="label">⏸️ Waiting code</div><div class="value">{escape(header["waiting_code"] or "—")}</div></div>
    <div class="stat-card{' alert' if header["stale"] and header["stale"] != "0" else ''}"><div class="label">Stale (&gt;SLA)</div><div class="value">{escape(header["stale"] or "—")}</div></div>
    <div class="stat-card"><div class="label">Total entries</div><div class="value">{escape(header["total_entries"] or "—")}</div></div>
  </div>
  <p style="color:{TEXT_FAINT}; font-size:0.85rem; margin-top:0;">Last touched: {escape(header["last_touched_resolved"] or "—")}</p>

  <h3>Action queue (oldest first)</h3>
  {action_html}

  <!-- STREAMS -->
  <span class="gold-rule"></span>
  <p class="eyebrow">Four parallel streams</p>
  <h2>What's running in parallel</h2>
  {streams_html}

  <!-- REDLINE -->
  <span class="gold-rule"></span>
  <p class="eyebrow">Outstanding REDLINE rework — gating the FCFCOA filing</p>
  <h2>Six items between current drafts and witnessing</h2>
  <table class="redline-table">
    <thead>
      <tr><th>Item</th><th>Para</th><th>Summary</th><th>Status</th><th>Input from</th></tr>
    </thead>
    <tbody>
      {redline_html}
    </tbody>
  </table>

  <!-- DRAFTS -->
  <span class="gold-rule"></span>
  <p class="eyebrow">Drafts folder · markdown source-of-truth</p>
  <h2>Current drafts ({len(drafts)})</h2>
  <table class="drafts-table">
    <thead>
      <tr><th>File</th><th>Size</th><th>Modified</th></tr>
    </thead>
    <tbody>
      {drafts_html}
    </tbody>
  </table>

  <!-- FOLDER STATS -->
  <h3>Folder counts</h3>
  <div class="folder-stats">{stats_html}</div>

  <!-- RECENT ACTIVITY -->
  <span class="gold-rule"></span>
  <p class="eyebrow">Recent activity · last 5 entries from PAIR.md</p>
  <h2>Latest log entries</h2>
  {entries_html}

</div>

<footer>
  <div class="container">
    Generated by Metis matter-dashboard · re-run any time at <code>python3 ~/Desktop/metis-cortex/prototypes/matter_dashboard.py</code> · pattern-based, deterministic, &lt;1 sec.<br>
    Tool: <a href="file://{escape(str(Path(__file__).resolve()))}">matter_dashboard.py</a> · Consistency report: <a href="file:///Users/kritsotakis/Desktop/metis-cortex/CONSISTENCY-REPORT-{date.today().isoformat()}.md">today's report</a>
  </div>
</footer>

</body>
</html>
'''
    return html


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
        else Path.home() / "Desktop/metis-cortex/dashboard.html"
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    pair_text = ""
    pair_path = matter / "PAIR.md"
    if pair_path.is_file():
        pair_text = pair_path.read_text(encoding="utf-8", errors="ignore")

    header = parse_pair_header(pair_text)
    header["last_touched_resolved"] = derive_last_touched(matter, pair_text, header["last_touched"])
    entries = parse_pair_entries(pair_text, n=5)
    stats = folder_stats(matter)
    drafts = list_drafts(matter)

    html = render_html(matter, header, entries, stats, drafts)
    output.write_text(html, encoding="utf-8")

    print(f"matter: {matter}")
    print(f"streams: {len(STREAMS)}")
    print(f"redline items: {len(REDLINE_ITEMS)}")
    print(f"drafts: {len(drafts)}")
    print(f"recent entries: {len(entries)}")
    print(f"dashboard: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
