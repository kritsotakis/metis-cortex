"""
Matter Pack assembler (M6) — the Stage-12 handoff bundle.

Assembles: triage summary + T1 inventory + workflow state + draft register +
latest critique findings + open questions → single branded HTML, rendered to
PDF via headless Chrome (same pipeline as the info one-pager).

Every page carries the DRAFT watermark. Output lands in METIS_HOME.
"""

from __future__ import annotations

import html
import subprocess
import sys
from datetime import date
from pathlib import Path

from . import DEFAULT_MATTER, METIS_HOME
from . import rails
from .inventory import scan
from .state_machine import MatterState, Stage

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page{size:A4;margin:14mm 14mm 16mm}
body{font-family:Inter,-apple-system,Helvetica,Arial,sans-serif;color:#1b2433;font-size:10.5px;line-height:1.45}
h1{font-family:Georgia,serif;color:#0f1e3d;font-size:22px;border-bottom:2px solid #c9a84c;padding-bottom:6px}
h2{font-family:Georgia,serif;color:#0f1e3d;font-size:14px;margin-top:18px}
table{border-collapse:collapse;width:100%;margin:8px 0}
th,td{border:1px solid #ddd;padding:4px 7px;text-align:left;vertical-align:top}
th{background:#f5f0e8;color:#0f1e3d}
.banner{background:#0f1e3d;color:#c9a84c;font-weight:700;padding:8px 12px;border-radius:3px;margin:0 0 14px}
.muted{color:#54607a;font-size:9px}
pre{white-space:pre-wrap;background:#faf7f0;padding:8px;border-left:3px solid #c9a84c;font-size:9.5px}
"""


def _latest(glob_pat: str) -> Path | None:
    hits = sorted(METIS_HOME.glob(glob_pat))
    return hits[-1] if hits else None


def build_html(matter: Path) -> str:
    st = MatterState(matter)
    results = scan(matter)
    icon = {"present": "✅", "partial": "🟡", "missing": "🔴"}

    inv_rows = "".join(
        f"<tr><td>{html.escape(r.item.name)}</td><td>{icon[r.state]} {r.state}</td>"
        f"<td>{html.escape(r.item.source_system)}</td>"
        f"<td>{html.escape(', '.join(r.item.affidavit_refs) or '—')}</td></tr>"
        for r in results
    )
    drafts_dir = matter / "drafts"
    drafts = sorted(drafts_dir.glob("*.md")) if drafts_dir.is_dir() else []
    draft_rows = "".join(
        f"<tr><td>{html.escape(d.name)}</td>"
        f"<td>{date.fromtimestamp(d.stat().st_mtime).isoformat()}</td></tr>"
        for d in drafts
    )
    critique = _latest(f"CRITIQUE-{matter.name.upper()}-*.md")
    critique_block = (
        f"<pre>{html.escape(critique.read_text(errors='ignore')[:8000])}</pre>"
        if critique else "<p class='muted'>No critique run on file — run <code>metis critique</code>.</p>"
    )
    open_items = "".join(
        f"<li><b>{html.escape(r.item.name)}</b> — {r.state}; retrieval: {r.item.retrieval} "
        f"via {html.escape(r.item.source_system)}. {html.escape(r.item.notes)}</li>"
        for r in results if r.state != "present"
    ) or "<li>None — all template items detected present.</li>"

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="banner">{rails.DRAFT_BANNER} — assembled by Metis for the matter owner's own use</div>
<h1>Matter Pack — {html.escape(matter.name)}</h1>
<p class="muted">Template T1 (DPO / s.111C stay) · generated {date.today().isoformat()} ·
workflow stage: {st.stage.value} · {rails.DISCLAIMER}</p>

<h2>1 · Triage summary</h2>
<p>Matter family: child-support court (DPO / s.111C stay). Framework: FCFCOA application.
Urgency gate: DPO restricting travel qualifies as an urgency trigger.</p>

<h2>2 · Document inventory (T1)</h2>
<table><tr><th>Item</th><th>Status</th><th>Source system</th><th>Affidavit refs</th></tr>{inv_rows}</table>

<h2>3 · Draft register</h2>
<table><tr><th>Draft</th><th>Last modified</th></tr>{draft_rows}</table>

<h2>4 · Latest adversarial critique</h2>
{critique_block}

<h2>5 · Open questions for the solicitor</h2>
<ul>{open_items}</ul>

<p class="muted">{rails.LAWYER_FLAG}</p>
</body></html>"""


def run(matter: Path | None = None) -> Path:
    matter = (matter or DEFAULT_MATTER).resolve()
    html_path = METIS_HOME / f"MATTER-PACK-{matter.name.upper()}-{date.today().isoformat()}.html"
    pdf_path = html_path.with_suffix(".pdf")
    html_path.write_text(build_html(matter))
    try:
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
            capture_output=True, timeout=60, check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    st = MatterState(matter)
    st.advance(Stage.MATTER_PACK, f"pack generated → {pdf_path.name}")
    out = pdf_path if pdf_path.exists() else html_path
    print(f"✅ matter pack → {out}")
    return out


if __name__ == "__main__":
    run(Path(sys.argv[1]) if len(sys.argv) > 1 else None)
