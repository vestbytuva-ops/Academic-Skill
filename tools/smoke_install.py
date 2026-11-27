"""Try project and user installs with the real skills CLI in disposable directories."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
NAME = "academic-skill"


def smoke(cli, source):
    skill = ROOT / "skills" / NAME
    resources = [
        path.relative_to(skill)
        for folder in ("references", "scripts", "assets", "evals")
        for path in (skill / folder).glob("*")
        if path.is_file()
    ]
    resources.extend(map(Path, ("SKILL.md", "agents/openai.yaml")))
    with TemporaryDirectory() as scratch:
        tmp = Path(scratch)
        home = tmp / "user"
        home.mkdir()
        env = {
            **os.environ, "CI": "1", "HOME": str(home), "USERPROFILE": str(home),
            "CODEX_HOME": str(home / ".codex"), "XDG_CONFIG_HOME": str(home / ".config"),
            "XDG_DATA_HOME": str(home / ".local/share"), "APPDATA": str(home / "AppData/Roaming"),
            "LOCALAPPDATA": str(home / "AppData/Local"),
        }
        for scope in ("project", "user"):
            project = tmp / f"{scope}-install"
            project.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=project, env=env, check=True)
            flags = ["--skill", NAME, "-g"] if scope == "user" else []
            subprocess.run([*cli, "add", source, *flags, "-a", "codex", "--copy", "-y"],
                           cwd=project, check=True, env=env)
            destination = (home if scope == "user" else project) / ".agents/skills"
            actual = {p.parent.name for p in destination.glob("*/SKILL.md")}
            if actual != {NAME}:
                raise ValueError(f"{scope}: expected {NAME}, found {sorted(actual)}")
            for path in resources:
                if not (destination / NAME / path).is_file():
                    raise ValueError(f"{scope}: missing {path} from {NAME}")
            print(f"{scope}: installed one {NAME} with its guidance and resources")


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
