import argparse
from pathlib import Path

from orchestrator import Pipeline


def main() -> None:
    parser = argparse.ArgumentParser(prog="bmad-auto", description="BMAD automation runner")
    sub = parser.add_subparsers(dest="command")

    run_p = sub.add_parser("run", help="Execute BMAD tasks pipeline")
    run_p.add_argument(
        "--mode",
        choices=["automatic", "semi-automatic", "interactive"],
        default="automatic",
        help="Automation mode",
    )

    args = parser.parse_args()

    if args.command == "run":
        repo_root = Path(__file__).resolve().parents[2]
        tasks_dir = repo_root / ".bmad-core" / "tasks"
        pipeline = Pipeline(tasks_dir)
        pipeline.run(mode=args.mode)
    else:
        parser.print_help()


if __name__ == "__main__":  # pragma: no cover
    main()
