"""Day 1: Inventory bootstrap from CSV/YAML to JSON.

Reads example CSV/YAML under `common/inventory/` and emits a normalized
JSON inventory at `common/outputs/devices.json`. This is a lightweight
Day 1 precursor to the Day 2 persistence lab (which adds SQLite).
"""

import json
from pathlib import Path
import sys

import yaml
from common.lib.logging_setup import setup_logging

log = setup_logging("inventory-bootstrap")

CSV_PATH = Path("common/inventory/devices.example.csv")
YAML_PATH = Path("common/inventory/devices.example.yaml")
OUT_PATH = Path("common/outputs/devices.json")


def load_inventory() -> list[dict]:
    if YAML_PATH.exists():
        data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
        devices = data.get("devices", data)
        if isinstance(devices, dict):
            devices = list(devices.values())
        return devices  # type: ignore
    if CSV_PATH.exists():
        # Minimal CSV loader; columns: name,host,os,platform,username,password,port
        import csv

        with CSV_PATH.open("r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        for r in rows:
            if "port" in r and r["port"]:
                try:
                    r["port"] = int(r["port"])  # type: ignore[assignment]
                except Exception:
                    r["port"] = 22
        return rows  # type: ignore
    log.error("No input inventory found at %s or %s", YAML_PATH, CSV_PATH)
    return []


def main() -> int:
    devices = load_inventory()
    if not devices:
        return 1
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(devices, indent=2), encoding="utf-8")
    log.info("Wrote inventory JSON with %s devices -> %s", len(devices), OUT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

