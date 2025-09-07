"""Generate story document."""
from __future__ import annotations

from pathlib import Path

from .checklists import ChecklistResult, run_checklist


def write_story(docs_dir: Path) -> ChecklistResult:
    """Write a simple user story document."""
    docs_dir.mkdir(parents=True, exist_ok=True)
    story_path = docs_dir / "story.md"
    content = (
        "# Story: Example Feature\n\n"
        "As a user, I want to see an example story so that I understand the workflow.\n"
        "Acceptance criteria outline the expected behavior and constraints.\n"
    )
    story_path.write_text(content + "\n")
    return run_checklist("story-draft-checklist.md", story_path)
