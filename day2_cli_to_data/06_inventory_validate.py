"""Validate inventory outputs for presence and required keys.

Checks `common/outputs/devices.json` exists and contains devices with
required fields. Beginner-friendly: prints a summary and exits 0/1.
"""

import json
from pathlib import Path
from typing import List, Dict

from common.lib.logging_setup import setup_logging

log = setup_logging("inventory-validate")

OUT = Path("common/outputs/devices.json")
REQUIRED = {"name", "host", "platform", "username"}


def main() -> int:
    if not OUT.exists():
        log.error("Missing %s; run day2_cli_to_data/00_inventory_persist.py first", OUT)
        return 1
    data: List[Dict] = json.loads(OUT.read_text(encoding="utf-8"))
    if not data:
        log.error("No devices found in %s", OUT)
        return 1
    ok = True
    for i, d in enumerate(data, 1):
        missing = REQUIRED - set(d.keys())
        if missing:
            ok = False
            log.error("Device %s missing keys: %s", i, ",".join(sorted(missing)))
    if ok:
        log.info("Inventory valid: %s devices, keys ok", len(data))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

