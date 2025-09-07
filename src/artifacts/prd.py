"""Generate PRD artifact."""
from __future__ import annotations

from pathlib import Path

from .checklists import ChecklistResult, run_checklist


def write_prd(docs_dir: Path) -> ChecklistResult:
    """Write a simple Product Requirements Document."""
    docs_dir.mkdir(parents=True, exist_ok=True)
    prd_path = docs_dir / "prd.md"
    content = (
        "# Product Requirements Document\n\n"
        "This is a minimal PRD generated for demonstration purposes.\n"
        "It captures the product vision, goals, and constraints in a single file.\n"
    )
    prd_path.write_text(content + "\n")
    return run_checklist("pm-checklist.md", prd_path)
