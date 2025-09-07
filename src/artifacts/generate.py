"""Generate documentation artifacts and run checklists."""
from __future__ import annotations

from pathlib import Path

from .architecture import write_architecture
from .prd import write_prd
from .story import write_story


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    docs_dir = repo_root / "docs"

    results = []
    results.append(write_prd(docs_dir))
    results.append(write_architecture(docs_dir))
    results.append(write_story(docs_dir))

    # Write final validation report
    report_lines = ["# Validation Report", "", "| Artifact | Checklist | Status |", "| --- | --- | --- |"]
    for r in results:
        report_lines.append(f"| {r.artifact} | {r.checklist} | {r.status} |")

    (docs_dir / "validation-report.md").write_text("\n".join(report_lines) + "\n")


if __name__ == "__main__":  # pragma: no cover
    main()
