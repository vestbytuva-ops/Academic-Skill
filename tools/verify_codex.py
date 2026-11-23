"""Verify that a real Codex app-server discovers every installed project or user skill."""
import argparse
import json
from pathlib import Path
import queue
import subprocess
import threading

ROOT = Path(__file__).resolve().parents[1]


def verify_labels(rows, catalog, scope):
    enabled = {}
    for row in rows:
        if row["scope"] == scope and row["enabled"] and row["name"] in catalog:
            label = (row.get("interface") or {}).get("displayName") or "(no display name)"
            enabled.setdefault(row["name"], set()).add(label)

    issues = []
    for name, entry in catalog.items():
        expected = entry["display_name"]
        labels = enabled.get(name, set())
        if not labels:
            issues.append(f"{name}: missing or disabled")
        elif expected not in labels:
            issues.append(f"{name}: expected {expected!r}, found {sorted(labels)}")
    if issues:
        raise RuntimeError(f"Incomplete Codex skill registration in {scope}: " + "; ".join(issues))


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
            print(f"Codex discovered {len(catalog)} enabled academic skills with matching display names in {scope}.")
        finally:
            server.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--scope", choices=["repo", "user"], default="repo")
    args = parser.parse_args()
    check(args.project.resolve(), args.scope)
