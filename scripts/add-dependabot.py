#!/usr/bin/env python3

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

from maintenance.is_fork import is_fork
from maintenance.util.log import logger

this_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd()).resolve()

user, _, repo_name = os.environ["REPOSITORY"].partition("/")
logger.debug(f"{user = }, {repo_name = }")


if is_fork("klieret", repo_name):
    logger.info(f"{repo_name} is a fork. skipping")
    sys.exit(0)

if Path(".github/").is_dir():
    logger.info("Copying dependabot.yml")
    source = this_dir / "dependabot.yml"
    target = cwd / ".github" / "dependabot.yml"
    shutil.copy(source, target)
else:
    logger.info("No .github. Skipping")
