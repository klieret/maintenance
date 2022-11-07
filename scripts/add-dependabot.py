#!/usr/bin/env python3

from __future__ import annotations

import os
import shutil
from pathlib import Path

this_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd()).resolve()


if Path(".github/").is_dir():
    source = this_dir / "dependabot.yml"
    target = cwd / ".github" / "dependabot.yml"
    shutil.copy(source, target)
