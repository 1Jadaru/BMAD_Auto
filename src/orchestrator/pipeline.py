import os
from pathlib import Path
from typing import List

from .registry import StepRegistry


class Pipeline:
    """Execution pipeline for BMAD tasks."""

    def __init__(self, tasks_dir: Path, registry: StepRegistry | None = None) -> None:
        self.tasks_dir = Path(tasks_dir)
        self.registry = registry or StepRegistry()
        self._load_tasks()

    def _load_tasks(self) -> None:
        files: List[Path] = sorted(self.tasks_dir.glob("*.md"))
        for path in files:
            name = path.stem

            def make_step(p: Path, n: str):
                def step() -> None:
                    print(f"=== Executing task: {n} ({p}) ===")
                    try:
                        with p.open("r", encoding="utf-8") as fh:
                            first = fh.readline().strip()
                            print(first)
                    except OSError as exc:
                        print(f"Failed to read {p}: {exc}")
                return step

            self.registry.register(name, make_step(path, name))

    def run(self, mode: str = "automatic") -> None:
        if mode == "automatic":
            for _, step in self.registry.steps():
                step()
        elif mode == "semi-automatic":
            for name, step in self.registry.steps():
                ans = input(f"Run task '{name}'? [Y/n]: ").strip().lower()
                if ans in ("", "y", "yes"):
                    step()
        elif mode == "interactive":
            remaining = list(self.registry.steps())
            while remaining:
                print("Select a task to run:")
                for i, (name, _) in enumerate(remaining, start=1):
                    print(f"{i}. {name}")
                print("0. Exit")
                try:
                    choice = int(input("Choice: "))
                except ValueError:
                    continue
                if choice == 0:
                    break
                if 1 <= choice <= len(remaining):
                    name, step = remaining.pop(choice - 1)
                    step()
        else:
            raise ValueError(f"Unknown mode: {mode}")
