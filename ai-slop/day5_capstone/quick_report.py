"""Quick offline report combining lab outputs.

Reads syslog events, NAPALM results, SNMP interfaces if present and
writes a small summary JSON + prints a human-friendly summary.
"""

import json
from pathlib import Path
from typing import Dict, Any

from common.lib.logging_setup import setup_logging

log = setup_logging("quick-report")

SYSLOG = Path("common/outputs/syslog_events.json")
NAPALM = Path("common/outputs/napalm_results.json")
SNMP = Path("common/outputs/snmp_ifaces.json")
OUT = Path("common/outputs/report.json")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    except Exception as e:
        log.warning("Failed to read %s: %s", path, e)
        return None


def main() -> None:
    syslog = load_json(SYSLOG) or []
    napalm = load_json(NAPALM) or {}
    snmp = load_json(SNMP) or []

    syslog_count = len(syslog)
    link_events = sum(1 for e in syslog if e.get("event") == "link_state")
    devices = list(napalm.keys())
    up_ifaces = sum(1 for r in snmp if int(r.get("ifOperStatus", 2)) == 1)

    summary: Dict[str, Any] = {
        "syslog_events": syslog_count,
        "link_state_events": link_events,
        "napalm_devices": devices,
        "snmp_up_ifaces": up_ifaces,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    log.info("Summary -> %s", OUT)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

