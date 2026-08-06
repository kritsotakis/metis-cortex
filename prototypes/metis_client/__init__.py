"""
metis_client — Phase 1 Metis client co-pilot (Metis-for-Peter).

Personal-use build: Peter is the only user (zero third-party UPL exposure).
Lane discipline: reads the matter folder READ-ONLY; all product state and
outputs live under METIS_HOME, never inside the matter folder.

Modules:
  template_t1    — T1 (DPO / s.111C stay) matter template, per
                   CLIENT-INTAKE-REFERENCE-2026-06-01.md Section F
  state_machine  — workflow: triage → inventory → retrieve → process
                   → critique → matter_pack
  inventory      — read-only scan of the matter folder vs the template
  rails          — UPL safe-harbour rails (hard-coded, not model-discretion)
"""

from pathlib import Path

PROTOTYPES_DIR = Path(__file__).resolve().parent.parent
METIS_HOME = PROTOTYPES_DIR.parent
DEFAULT_MATTER = Path.home() / "Desktop/dpo"
STATE_DIR = METIS_HOME / ".metis-state"  # product state lives OUTSIDE the matter folder
