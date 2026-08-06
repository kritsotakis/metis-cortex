"""
T1 matter template — Child support court (DPO / s.111C stay).

Canonical source: CLIENT-INTAKE-REFERENCE-2026-06-01.md Section F.
Each item knows: why it's needed, which source system holds it, how it's
retrieved in Phase 1 (upload / co-pilot / request-letter), and which
affidavit paragraphs consume it.

`detect_patterns` are lowercase substrings/regex fragments matched against
filenames AND fact-extract text in the matter folder to auto-detect presence.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MatterItem:
    id: str
    name: str
    why: str
    source_system: str
    retrieval: str          # upload | copilot | request_letter | client_records
    detect_patterns: tuple[str, ...]
    affidavit_refs: tuple[str, ...] = ()
    notes: str = ""


T1_ITEMS: tuple[MatterItem, ...] = (
    MatterItem(
        id="sa_correspondence",
        name="All Services Australia correspondence in the matter",
        why="Foundation of the application",
        source_system="CSAOnline",
        retrieval="copilot",
        detect_patterns=("sa_", "services australia", "csa", "child support agency"),
        notes="18 PDFs previously pulled manually from CSAOnline",
    ),
    MatterItem(
        id="dpo_copy",
        name="DPO copy (s.72D, issued under CSRC Act)",
        why="Establishes existence + terms of the order being challenged",
        source_system="Services Australia (admin request / FOI fallback)",
        retrieval="request_letter",
        detect_patterns=("dpo cop", "departure prohibition order", "dpo_copy", "s.72d", "s72d"),
        affidavit_refs=("Para 16",),
        notes="Request letter = drafts/06; FOI fallback = drafts/07",
    ),
    MatterItem(
        id="ati_history",
        name="Income/ATI history showing distortion (7 NOAs, 2018-19 to 2024-25)",
        why="Justifies stay — current assessment unfair vs income reality",
        source_system="myGov → ATO",
        retrieval="copilot",
        detect_patterns=("noa", "notice of assessment", "ati", "taxable income"),
        affidavit_refs=("Para 19",),
        notes="One-off 2019-20 CGT spike (Tempe sale) is the distortion",
    ),
    MatterItem(
        id="one_off_event",
        name="One-off income event documentation (Tempe sale + CGT schedule + net proceeds)",
        why="Matter turns on the CGT event",
        source_system="Conveyancer/accountant records",
        retrieval="request_letter",
        detect_patterns=("tempe", "cgt", "capital gain", "net proceeds", "sale contract"),
        affidavit_refs=("Para 19", "Para 23B"),
        notes="Wesley/accountant email = drafts/08",
    ),
    MatterItem(
        id="current_income",
        name="Current income evidence (workers comp + DSK business income)",
        why="What payer is actually earning now",
        source_system="Insurer payment summary + business records",
        retrieval="upload",
        detect_patterns=("workers comp", "wc payment", "1,680", "1680", "dsk income", "payment summary"),
        affidavit_refs=("Para 23B", "Para 24(a)"),
        notes="WC @ $1,680/wk gross since Jan 2024",
    ),
    MatterItem(
        id="bankruptcy_status",
        name="Bankruptcy status (AFSA petition)",
        why="Affects ability to pay + asset pool",
        source_system="AFSA / NPII",
        retrieval="copilot",
        detect_patterns=("afsa", "bankrupt", "npii", "statement of affairs", "soa"),
        affidavit_refs=("Para 23C",),
    ),
    MatterItem(
        id="travel_necessity",
        name="Travel necessity evidence (hardship-based)",
        why="Why travel is needed if DPO lift sought",
        source_system="Client records",
        retrieval="upload",
        detect_patterns=("travel", "hardship"),
    ),
    MatterItem(
        id="interim_payment",
        name="Proposed interim payment evidence (defensible per Critique F4)",
        why="What payer can realistically pay during stay",
        source_system="Business records",
        retrieval="upload",
        detect_patterns=("interim payment", "50% net", "proposed payment"),
        affidavit_refs=("Para 24(a)",),
        notes="Rewritten from $50/week (read as contempt) to 50% net DSK income",
    ),
    MatterItem(
        id="prior_coa",
        name="Prior change-of-assessment applications + rejection reasons",
        why="Procedural history",
        source_system="CSAOnline / client records",
        retrieval="copilot",
        detect_patterns=("change of assessment", "reason 8", "8a", "8b", "s.98c", "s98c", "coa"),
        notes="April 2025 Reason 8A rejected (s.98C 18-month limit); Sarah filed Reason 8B 1 Jun 2026",
    ),
    MatterItem(
        id="trust_disclosure",
        name="Trust interests — full disclosure (Kritsotakis Family Trust)",
        why="Required even as discretionary beneficiary (Critique E7)",
        source_system="ASIC Connect / trust deed / accountant",
        retrieval="request_letter",
        detect_patterns=("trust", "45 984 876 899", "45984876899", "kritsotakis investments", "153 844 136"),
        affidavit_refs=("Para 23C",),
    ),
)

# Process gates the engine must surface for ANY family-law matter
# (from CLIENT-INTAKE-REFERENCE "Family-law process gates")
PROCESS_GATES: tuple[tuple[str, str], ...] = (
    ("fv_screening", "Family violence screening (s4AB + Lighthouse) — every matter"),
    ("disclosure_duty", "Full + frank financial disclosure (s71B/s90RI) — ongoing, breach = contempt/costs"),
    ("urgency", "Urgency triggers — DPO blocking travel qualifies"),
)


@dataclass
class ItemStatus:
    item: MatterItem
    state: str            # present | partial | missing
    evidence: list[str] = field(default_factory=list)  # matching file paths


def template_summary() -> str:
    lines = [f"T1 — DPO / s.111C stay · {len(T1_ITEMS)} required items"]
    for it in T1_ITEMS:
        refs = f"  → {', '.join(it.affidavit_refs)}" if it.affidavit_refs else ""
        lines.append(f"  [{it.retrieval:>14}] {it.name}{refs}")
    return "\n".join(lines)
