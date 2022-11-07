from __future__ import annotations

import json
import subprocess
import sys


def is_fork(user: str, repo_name: str) -> bool:
    r = subprocess.run(
        ["gh", "api", "--method", "GET", f"/repos/{user}/{repo_name}"],
        capture_output=True,
    )
    asdct = json.loads(r.stdout)
    return asdct["fork"]


if __name__ == "__main__":
    print(is_fork(*sys.argv[1:]))
