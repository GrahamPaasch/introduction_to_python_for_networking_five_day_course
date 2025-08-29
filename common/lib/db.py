import os
import sqlite3
from typing import Iterable, Dict, Any

DB_PATH = os.getenv("NETAUTO_DB", "common/outputs/inventory.sqlite")


def ensure_db(path: str = DB_PATH) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS devices (name TEXT PRIMARY KEY, host TEXT, os TEXT, platform TEXT, username TEXT, port INTEGER)"
    )
    return conn


def upsert_devices(devices: Iterable[Dict[str, Any]], path: str = DB_PATH) -> None:
    conn = ensure_db(path)
    with conn:
        for d in devices:
            conn.execute(
                "INSERT INTO devices(name, host, os, platform, username, port) VALUES(?,?,?,?,?,?) "
                "ON CONFLICT(name) DO UPDATE SET host=excluded.host, os=excluded.os, platform=excluded.platform, username=excluded.username, port=excluded.port",
                (d["name"], d["host"], d["os"], d["platform"], d["username"], int(d.get("port", 22))),
            )
    conn.close()
