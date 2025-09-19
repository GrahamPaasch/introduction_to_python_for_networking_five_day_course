"""Parse sample syslog into structured JSON for beginners.
No external dependencies; safe offline lab.
"""

import json
import re
from pathlib import Path
from typing import Dict, List

from common.lib.logging_setup import setup_logging

log = setup_logging("syslog-parse")

SYSLOG_PATH = Path("common/fixtures/syslog.log")
OUT_PATH = Path("common/outputs/syslog_events.json")

RFC5424_RE = re.compile(
    r"^<(?P<pri>\d+)>1\s+(?P<ts>\S+)\s+(?P<host>\S+)\s+(?P<msg>.+)$"
)


def parse_line(line: str) -> Dict[str, str]:
    m = RFC5424_RE.match(line.strip())
    if not m:
        return {"raw": line.strip()}
    pri = int(m.group("pri"))
    facility = pri // 8
    severity = pri % 8
    msg = m.group("msg")
    # quick heuristics
    event = "other"
    iface = None
    if "LINK-3-UPDOWN" in msg:
        event = "link_state"
        m2 = re.search(r"Interface (\S+), changed state to (\w+)", msg)
        if m2:
            iface = m2.group(1)
    elif "CONFIG_I" in msg:
        event = "config"
    elif "SEC-" in msg:
        event = "security_log"
    return {
        "timestamp": m.group("ts"),
        "host": m.group("host"),
        "facility": str(facility),
        "severity": str(severity),
        "event": event,
        "interface": iface or "",
        "message": msg,
    }


def main() -> None:
    lines = SYSLOG_PATH.read_text(encoding="utf-8").splitlines()
    events: List[Dict[str, str]] = [parse_line(ln) for ln in lines if ln.strip()]
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(events, indent=2), encoding="utf-8")
    log.info("Parsed %s events -> %s", len(events), OUT_PATH)


if __name__ == "__main__":
    main()

