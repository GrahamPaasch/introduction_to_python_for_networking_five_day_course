"""Config diff demo (offline, stdlib-only).

Shows how to compute a unified diff between two config files.
Useful to explain idempotence and safe changes.
"""

import difflib
from pathlib import Path

from common.lib.logging_setup import setup_logging

log = setup_logging("config-diff")

BEFORE = Path("common/fixtures/config_before.txt")
AFTER = Path("common/fixtures/config_after.txt")


def main() -> None:
    before = BEFORE.read_text(encoding="utf-8").splitlines(keepends=True)
    after = AFTER.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = difflib.unified_diff(before, after, fromfile=str(BEFORE), tofile=str(AFTER))
    text = "".join(diff)
    if text:
        log.info("\n%s", text)
    else:
        log.info("No differences detected")


if __name__ == "__main__":
    main()

