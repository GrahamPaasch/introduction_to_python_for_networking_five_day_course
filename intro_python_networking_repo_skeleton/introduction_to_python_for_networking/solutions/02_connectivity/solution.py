"""Lab 02: Safe device connectivity with Netmiko.
- Read inventory from ../01_inventory/expected_output/inventory.json
- Implement safe_exec() to run vendor-appropriate show command
- Save raw outputs per device under expected_output/<host>.txt
- Provide an --offline flag to use fixtures instead of real devices.

Run:
    python solution.py [--offline]
"""
from __future__ import annotations
import json, pathlib, argparse, time

ROOT = pathlib.Path(__file__).parent
INV_JSON = ROOT.parent / "01_inventory" / "expected_output" / "inventory.json"
OUT = ROOT / "expected_output"; OUT.mkdir(exist_ok=True)
FIX = ROOT / "fixtures"; FIX.mkdir(exist_ok=True)

SHOWS = {
    "cisco_ios": "show ip interface brief",
    "juniper_junos": "show interfaces terse",
}

def safe_exec(dev: dict, offline: bool = False) -> str:
    if offline:
        fix = FIX / f"{dev['hostname']}.txt"
        return fix.read_text() if fix.exists() else f"offline fixture missing for {dev['hostname']}\n"
    # Real devices: lazy-import netmiko
    from netmiko import ConnectHandler  # type: ignore
    conn = ConnectHandler(
        device_type=dev["platform"], host=dev["ip"],
        username=dev["username"], password=dev["password"],
        secret=dev.get("secret") or None, fast_cli=False, timeout=20,
    )
    try:
        if dev.get("secret"):
            conn.enable()
        cmd = SHOWS.get(dev["platform"], "show version")
        return conn.send_command(cmd, read_timeout=30)
    finally:
        conn.disconnect()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()

    devices = json.loads(INV_JSON.read_text())
    for d in devices:
        out = safe_exec(d, offline=args.offline)
        (OUT / f"{d['hostname']}.txt").write_text(out)
        print(f"[{time.strftime('%H:%M:%S')}] {d['hostname']}: wrote {OUT / (d['hostname']+'.txt')}")
    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
