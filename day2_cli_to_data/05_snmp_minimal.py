"""Minimal SNMP example (offline-first).

If OFFLINE=1 or pysnmp is unavailable, reads from fixture
`common/fixtures/snmp_ifTable.json` and writes a normalized
`common/outputs/snmp_ifaces.json` file. If pysnmp is available and
OFFLINE is not set, attempts a simple GETNEXT walk of ifDescr and
ifOperStatus.

Beginner-friendly: no additional dependencies required to complete.
"""

import json
import os
from typing import Dict, List
from pathlib import Path

from common.lib.logging_setup import setup_logging

log = setup_logging("snmp-minimal")

OFFLINE = os.getenv("OFFLINE", "false").lower() in {"1", "true", "yes"}
OUT_PATH = Path("common/outputs/snmp_ifaces.json")


def from_fixture() -> List[Dict]:
    with open("common/fixtures/snmp_ifTable.json", "r", encoding="utf-8") as f:
        rows: List[Dict] = json.load(f)
    return rows


def from_live() -> List[Dict]:
    try:
        from pysnmp.hlapi import (  # type: ignore
            CommunityData,
            SnmpEngine,
            UdpTransportTarget,
            ContextData,
            ObjectType,
            ObjectIdentity,
            nextCmd,
        )
    except Exception as e:
        log.warning("pysnmp not available: %s; falling back to fixture", e)
        return from_fixture()

    host = os.getenv("SNMP_HOST", "127.0.0.1")
    community = os.getenv("SNMP_COMMUNITY", "public")
    timeout = int(os.getenv("SNMP_TIMEOUT", "2"))
    retries = int(os.getenv("SNMP_RETRIES", "0"))

    descr_oid = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")
    oper_oid = ObjectIdentity("1.3.6.1.2.1.2.2.1.8")

    descr_map: Dict[int, str] = {}
    oper_map: Dict[int, int] = {}

    def walk(oid: ObjectIdentity):
        for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=1),
            UdpTransportTarget((host, 161), timeout=timeout, retries=retries),
            ContextData(),
            ObjectType(oid),
            lexicographicMode=False,
        ):
            if errorIndication:
                raise RuntimeError(errorIndication)
            if errorStatus:
                raise RuntimeError("%s at %s" % (errorStatus.prettyPrint(), errorIndex))
            for varBind in varBinds:
                yield varBind

    try:
        for vb in walk(descr_oid):
            oid, val = vb
            idx = int(str(oid).split(".")[-1])
            descr_map[idx] = str(val)
        for vb in walk(oper_oid):
            oid, val = vb
            idx = int(str(oid).split(".")[-1])
            oper_map[idx] = int(val)
    except Exception as e:
        log.warning("SNMP walk failed: %s; using fixture", e)
        return from_fixture()

    rows: List[Dict] = []
    for idx, descr in sorted(descr_map.items()):
        rows.append({
            "ifIndex": idx,
            "ifDescr": descr,
            "ifType": 6,
            "ifOperStatus": oper_map.get(idx, 2),
        })
    return rows


def main() -> None:
    rows = from_fixture() if OFFLINE else from_live()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    up = sum(1 for r in rows if int(r.get("ifOperStatus", 2)) == 1)
    down = sum(1 for r in rows if int(r.get("ifOperStatus", 2)) != 1)
    log.info("SNMP interfaces: total=%s up=%s down=%s -> %s", len(rows), up, down, OUT_PATH)


if __name__ == "__main__":
    main()

