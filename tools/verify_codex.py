"""Check that Codex discovers the integrated skill at the requested scope."""
import argparse
import json
from pathlib import Path
import queue
import subprocess
import threading

ROOT = Path(__file__).resolve().parents[1]
FORMER_LABELS = {
    "academic-core": "Academic Core", "personal-voice": "Academic Personal Voice",
    "academic-writing": "Academic Writing", "humanizer": "Academic Copyediting",
    "academic-critic": "Academic Critic", "research-integrity": "Academic Research Integrity",
    "learning-coach": "Academic Learning Coach", "exam-preparation": "Academic Exam Preparation",
    "presentation-engine": "Academic Presentations", "office-integration": "Academic Office Files",
    "quality-assurance": "Academic Quality Assurance",
}


def verify_labels(rows, catalog, scope):
    active = [row for row in rows if row["scope"] == scope and row["enabled"]]
    legacy = set()
    for row in active:
        previous = FORMER_LABELS.get(row["name"])
        label = (row.get("interface") or {}).get("displayName")
        if previous and label in (previous, previous.removeprefix("Academic ")):
            legacy.add(row["name"])
    if legacy:
        raise RuntimeError(f"Former specialist registrations in {scope}: {', '.join(sorted(legacy))}")
    expected = catalog["academic-skill"]["display_name"]
    labels = [(r.get("interface") or {}).get("displayName") for r in active if r["name"] == "academic-skill"]
    if labels != [expected]:
        raise RuntimeError(f"Expected one enabled academic-skill named {expected!r} in {scope}, found {labels}")


def check(project, scope):
    catalog = json.loads((ROOT / "tools/catalog.json").read_text(encoding="utf-8"))
    replies = queue.Queue()
    with subprocess.Popen(["codex", "app-server"], cwd=project, text=True, encoding="utf-8",
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE) as server:
        def read():
            for line in server.stdout:
                replies.put(json.loads(line))
            replies.put(None)

        threading.Thread(target=read, daemon=True).start()

        def request(method, params, idx=None):
            message = {"method": method, "params": params}
            if idx is not None:
                message["id"] = idx
            server.stdin.write(json.dumps(message) + "\n")
            server.stdin.flush()
            if idx is None:
                return
            while True:
                reply = replies.get(timeout=30)
                if reply is None:
                    raise RuntimeError("Codex app-server exited before replying")
                if reply.get("id") == idx:
                    if "error" in reply:
                        raise RuntimeError(reply["error"])
                    return reply["result"]
        try:
            request("initialize", {"clientInfo": {"name": "academic-skill-check", "version": "1"},
                                   "capabilities": {"experimentalApi": True}}, 1)
            request("initialized", {})
            response = request("skills/list", {"cwds": [str(project)], "forceReload": True}, 2)
            rows = response["data"][0]["skills"]
            verify_labels(rows, catalog, scope)
            print(f"Codex discovered one enabled Academic Skill in {scope}.")
        finally:
            server.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--scope", choices=["repo", "user"], default="repo")
    args = parser.parse_args()
    check(args.project.resolve(), args.scope)
