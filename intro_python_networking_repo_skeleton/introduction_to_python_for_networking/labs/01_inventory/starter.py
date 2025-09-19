"""Lab 01: Build an inventory from CSV/YAML and export to JSON + SQLite.

Tasks:
- Read devices from devices.csv (preferred) or devices.yaml
- Normalize fields -> list[dict]
- Write JSON to expected_output/inventory.json
- Write SQLite DB to expected_output/inventory.sqlite (table: devices)

Run:
    python starter.py
"""
from __future__ import annotations
import csv, json, sqlite3, pathlib, sys
import yaml  # type: ignore

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "expected_output"
OUT.mkdir(exist_ok=True)

def read_csv(path: pathlib.Path) -> list[dict]:
    with path.open() as f:
        return [row for row in csv.DictReader(f)]

def read_yaml(path: pathlib.Path) -> list[dict]:
    with path.open() as f:
        data = yaml.safe_load(f) or {}
    return list(data.get("devices", []))

def normalize(devs: list[dict]) -> list[dict]:
    fields = ["hostname","ip","platform","username","password","secret"]
    out = []
    for d in devs:
        out.append({k: (str(d.get(k)) if d.get(k) is not None else "") for k in fields})
    return out

def write_json(devs: list[dict], path: pathlib.Path) -> None:
    path.write_text(json.dumps(devs, indent=2))

def write_sqlite(devs: list[dict], path: pathlib.Path) -> None:
    con = sqlite3.connect(path)
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS devices(
              hostname TEXT, ip TEXT, platform TEXT,
              username TEXT, password TEXT, secret TEXT
            )
        """)
        con.execute("DELETE FROM devices")
        con.executemany(
            "INSERT INTO devices VALUES (:hostname,:ip,:platform,:username,:password,:secret)",
            devs,
        )
    con.close()

def main() -> int:
    src = ROOT / "devices.csv"
    if not src.exists():
        src = ROOT / "devices.yaml"
    devs = normalize(read_csv(src) if src.suffix == ".csv" else read_yaml(src))
    write_json(devs, OUT / "inventory.json")
    write_sqlite(devs, OUT / "inventory.sqlite")
    print(f"Wrote {OUT/'inventory.json'} and {OUT/'inventory.sqlite'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
