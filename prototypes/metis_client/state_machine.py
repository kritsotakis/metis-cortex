"""
Workflow state machine: triage → inventory → retrieve → process → critique → matter_pack.

State persists to METIS_HOME/.metis-state/<matter-name>.json — deliberately
OUTSIDE the matter folder (lane discipline: the matter folder is read-only
to Metis; legal substance stays with the DPO session).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

from . import STATE_DIR


class Stage(str, Enum):
    TRIAGE = "triage"
    INVENTORY = "inventory"
    RETRIEVE = "retrieve"
    PROCESS = "process"
    CRITIQUE = "critique"
    MATTER_PACK = "matter_pack"


STAGE_ORDER = list(Stage)


class MatterState:
    """Persisted workflow state for one matter."""

    def __init__(self, matter: Path):
        self.matter = matter.resolve()
        self.path = STATE_DIR / f"{self.matter.name}.json"
        self.data: dict = {
            "matter": str(self.matter),
            "template": "T1",
            "stage": Stage.TRIAGE.value,
            "history": [],       # [{stage, at, note}]
            "items": {},         # item_id -> {state, evidence, updated}
        }
        if self.path.exists():
            try:
                self.data.update(json.loads(self.path.read_text()))
            except (json.JSONDecodeError, OSError):
                pass  # corrupt state falls back to fresh; history rebuilt on next save

    # -- persistence -------------------------------------------------------
    def save(self) -> None:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2))

    # -- stage transitions --------------------------------------------------
    @property
    def stage(self) -> Stage:
        return Stage(self.data["stage"])

    def advance(self, to: Stage, note: str = "") -> None:
        self.data["stage"] = to.value
        self.data["history"].append(
            {"stage": to.value, "at": datetime.now(timezone.utc).isoformat(), "note": note}
        )
        self.save()

    # -- item tracking -------------------------------------------------------
    def set_item(self, item_id: str, state: str, evidence: list[str]) -> None:
        self.data["items"][item_id] = {
            "state": state,
            "evidence": evidence[:20],
            "updated": datetime.now(timezone.utc).isoformat(),
        }

    def summary(self) -> str:
        counts: dict[str, int] = {}
        for rec in self.data["items"].values():
            counts[rec["state"]] = counts.get(rec["state"], 0) + 1
        parts = [f"{k}: {v}" for k, v in sorted(counts.items())]
        return f"stage={self.stage.value} · items[{', '.join(parts) or 'unscanned'}]"
