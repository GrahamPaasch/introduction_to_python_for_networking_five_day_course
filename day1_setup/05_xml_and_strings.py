"""Tiny XML parsing + string methods demo (stdlib-only).

Reads `common/fixtures/devices.xml`, shows basic ElementTree parsing
and Python string methods like split(), startswith(), lower(), strip().
Writes a small JSON summary for later labs.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict

from common.lib.logging_setup import setup_logging

log = setup_logging("xml-strings")

XML_PATH = Path("common/fixtures/devices.xml")
OUT_PATH = Path("common/outputs/devices_from_xml.json")


def normalize_vendor(v: str) -> str:
    v = v.strip().lower()
    if v.startswith("cisco"):
        return "cisco"
    if v.startswith("juniper"):
        return "juniper"
    return v


def main() -> None:
    tree = ET.parse(str(XML_PATH))
    root = tree.getroot()
    items: List[Dict] = []
    for dev in root.findall("device"):
        name = (dev.findtext("name") or "").strip()
        ip = (dev.findtext("ip") or "").strip()
        vendor = normalize_vendor(dev.findtext("vendor") or "")
        location = (dev.findtext("location") or "").strip()
        # simple string method demo
        site_words = location.split()
        site_code = "-".join(w.lower() for w in site_words if w)
        items.append({
            "name": name,
            "ip": ip,
            "vendor": vendor,
            "site": site_code,
            "is_edge": name.startswith("edge-"),
        })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(items, indent=2), encoding="utf-8")
    log.info("Parsed %s devices -> %s", len(items), OUT_PATH)


if __name__ == "__main__":
    main()

