from __future__ import annotations

import json
import subprocess
import sys

from maintenance.util.log import logger


def is_fork(user: str, repo_name: str) -> bool:
    """Return True if repository is a fork"""
    cmd = ["gh", "api", "--method", "GET", f"/repos/{user}/{repo_name}"]
    logger.debug(cmd)
    r = subprocess.run(
        cmd,
        capture_output=True,
    )
    asdct = json.loads(r.stdout)
    try:
        return asdct["fork"]
    except KeyError:
        logger.error("Didn't find 'fork' key")
        logger.debug(f"For reference, here's the whole output: {asdct}")
        raise


if __name__ == "__main__":
    print(is_fork(*sys.argv[1:]))
