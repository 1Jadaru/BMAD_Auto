"""Generate architecture document."""
from __future__ import annotations

from pathlib import Path

from .checklists import ChecklistResult, run_checklist


def write_architecture(docs_dir: Path) -> ChecklistResult:
    """Write a simple architecture document."""
    docs_dir.mkdir(parents=True, exist_ok=True)
    arch_path = docs_dir / "architecture.md"
    content = (
        "# Architecture Overview\n\n"
        "This document outlines the high-level system architecture.\n"
        "It describes the major components and how they interact.\n"
    )
    arch_path.write_text(content + "\n")
    return run_checklist("architect-checklist.md", arch_path)
