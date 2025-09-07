"""Utility functions for running checklists."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


CHECKLIST_DIR = Path(__file__).resolve().parents[2] / ".bmad-core" / "checklists"


@dataclass
class ChecklistResult:
    """Result from running a checklist."""

    artifact: str
    checklist: str
    status: str  # PASS, CONCERNS, or FAIL


def run_checklist(checklist_name: str, artifact_path: Path) -> ChecklistResult:
    """Run a checklist against an artifact.

    Since we don't have automated evaluation of checklist items, we use a
    simple heuristic based on artifact file size:
    - size == 0 bytes -> FAIL
    - size < 100 bytes -> CONCERNS
    - size >= 100 bytes -> PASS
    """
    checklist_path = CHECKLIST_DIR / checklist_name
    if not checklist_path.exists():
        raise FileNotFoundError(f"Checklist {checklist_name} not found")

    size = artifact_path.stat().st_size if artifact_path.exists() else 0
    if size == 0:
        status = "FAIL"
    elif size < 100:
        status = "CONCERNS"
    else:
        status = "PASS"

    return ChecklistResult(
        artifact=artifact_path.name,
        checklist=checklist_name,
        status=status,
    )
