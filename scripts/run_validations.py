"""Simple validation runner for classroom demos.

Runs a set of beginner-friendly validations and prints PASS/FAIL.
Use OFFLINE=1 to avoid all external calls.
"""

import os
import subprocess
from pathlib import Path

green = "\x1b[32m"
red = "\x1b[31m"
reset = "\x1b[0m"

ROOT = Path(__file__).resolve().parents[1]


def run(cmd, env=None):
    print(f"$ {' '.join(cmd)}")
    return subprocess.run(cmd, env=env or os.environ.copy())


def exists(path: str) -> bool:
    return (ROOT / path).exists()


def main() -> int:
    failures = 0
    env_offline = os.environ.copy()
    env_offline["OFFLINE"] = env_offline.get("OFFLINE", "1")  # default offline

    checks = [
        ("Day1 basics", ["python", "day1_setup/01_python_basics.py"], None, None),
        ("XML + strings", ["python", "day1_setup/05_xml_and_strings.py"], None, "common/outputs/devices_from_xml.json"),
        ("Inventory persist", ["python", "day2_cli_to_data/00_inventory_persist.py"], None, "common/outputs/inventory.sqlite"),
        ("Syslog parse", ["python", "day2_cli_to_data/04_syslog_parse.py"], None, "common/outputs/syslog_events.json"),
        ("SNMP minimal (offline)", ["python", "day2_cli_to_data/05_snmp_minimal.py"], env_offline, "common/outputs/snmp_ifaces.json"),
        ("NAPALM getters (offline)", ["python", "day2_cli_to_data/02_napalm_getters.py"], env_offline, "common/outputs/napalm_results.json"),
        ("RESTCONF (offline)", ["python", "day3_rest_and_json/01_restconf_requests.py"], env_offline, None),
        ("Junos REST (offline)", ["python", "day3_rest_and_json/02_junos_rest_httpx.py"], env_offline, None),
    ]

    for name, cmd, env, artifact in checks:
        print(f"\n== {name} ==")
        r = run(cmd, env)
        ok = r.returncode == 0 and (artifact is None or exists(artifact))
        print((green + "PASS" + reset) if ok else (red + "FAIL" + reset))
        failures += 0 if ok else 1

    print(f"\nSummary: {len(checks) - failures} passed / {len(checks)} total")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

