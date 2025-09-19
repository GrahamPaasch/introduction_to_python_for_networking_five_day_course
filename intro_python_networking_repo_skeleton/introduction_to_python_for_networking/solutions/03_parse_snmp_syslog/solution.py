"""Lab 03: Parse SNMP + syslog to produce a simple health report.

Offline mode only (fixtures): parse fixtures/snmp_walk.json and fixtures/syslog_samples.log
Compute per-device CPU/mem (or vendor-specific equivalents) and recent link flaps.
Write JSON report to expected_output/health_report.json

Run:
    python solution.py
"""
from __future__ import annotations
import json, pathlib, re, collections, datetime as dt

ROOT = pathlib.Path(__file__).parent
FIX = ROOT / "fixtures"
OUT = ROOT / "expected_output"; OUT.mkdir(exist_ok=True)

def parse_syslog(path: pathlib.Path) -> dict[str,int]:
    txt = path.read_text().splitlines()
    counts = collections.Counter()
    for line in txt:
        if "LINK" in line or "SNMP_TRAP_LINK" in line:
            # crude device name extraction
            parts = line.split()
            if len(parts) >= 3:
                dev = parts[2]
                counts[dev] += 1
    return dict(counts)

def main() -> int:
    snmp = json.loads((FIX / "snmp_walk.json").read_text())
    flaps = parse_syslog(FIX / "syslog_samples.log")
    report = {}
    for dev, oids in snmp.items():
        cpu = next((v for k,v in oids.items() if k.endswith(".2.1") or "13.1.8.0" in k), None)
        mem = next((v for k,v in oids.items() if k.endswith("57.0") or "13.1.11.0" in k), None)
        report[dev] = {"cpu_pct": cpu, "mem_pct": mem, "link_events": flaps.get(dev, 0)}
    (OUT / "health_report.json").write_text(json.dumps(report, indent=2))
    print(f"Wrote {(OUT/'health_report.json')}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
