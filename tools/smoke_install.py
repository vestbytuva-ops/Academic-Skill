"""Exercise the real skills CLI in disposable projects without modifying user installations."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def smoke(cli, source):
    names = set(json.loads((ROOT / "tools/catalog.json").read_text(encoding="utf-8")))
    with TemporaryDirectory() as scratch:
        for case, select, expected in (("all", "*", names), ("only", "research-integrity", {"research-integrity"}),
                                       ("umbrella", "academic-skill", {"academic-skill"})):
            project = Path(scratch) / case
            project.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=project, check=True)
            subprocess.run([*cli, "add", source, "--skill", select, "-a", "codex", "--copy", "-y"],
                           cwd=project, check=True, env={**os.environ, "CI": "1"})
            base = project / ".agents/skills"
            actual = {p.parent.name for p in base.glob("*/SKILL.md")}
            if actual != expected:
                raise ValueError(f"{case}: expected {sorted(expected)}, installed {sorted(actual)}")
            for name in expected:
                if not (base / name / "references/arbeidsgrunnlag.md").is_file():
                    raise ValueError(f"Installed {name} is missing its shared guidance")
            print(f"{case}: installed and verified {len(actual)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", help="Use an already installed skills executable")
    parser.add_argument("--source", default=str(ROOT), help="Checkout path or remote repository URL")
    args = parser.parse_args()
    if args.cli:
        executable = shutil.which(args.cli) or args.cli
        runner = [str(Path(executable).resolve())]
    else:
        runner = [shutil.which("npx") or "npx", "--yes", "skills@1.9.0"]
    source_path = Path(args.source)
    source = str(source_path.resolve()) if source_path.exists() else args.source
    smoke(runner, source)
