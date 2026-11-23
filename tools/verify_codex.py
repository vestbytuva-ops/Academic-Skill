"""Verify that a real Codex app-server discovers every installed project or user skill."""
import argparse
import json
from pathlib import Path
import queue
import subprocess
import threading

ROOT = Path(__file__).resolve().parents[1]


def check(project, scope):
    expected = set(json.loads((ROOT / "tools/catalog.json").read_text(encoding="utf-8")))
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
            found = {row["name"] for row in rows if row["scope"] == scope and row["enabled"]}
            missing = expected - found
            if missing:
                raise RuntimeError(f"Missing enabled skills in {scope}: {sorted(missing)}")
            print(f"Codex discovered {len(expected)} enabled academic skills with scope {scope}.")
        finally:
            server.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--scope", choices=["repo", "user"], default="repo")
    args = parser.parse_args()
    check(args.project.resolve(), args.scope)
