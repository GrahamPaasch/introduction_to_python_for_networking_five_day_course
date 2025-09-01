"""Junos REST API with httpx fallback to mocks if not configured."""

import os
import json
import httpx

from common.lib.logging_setup import setup_logging

log = setup_logging("junos-rest")

BASE = os.getenv("JUNOS_API_BASE", "")  # e.g., https://<host>/rpc/
USER = os.getenv("JUNOS_API_USER", "lab")
PASS = os.getenv("JUNOS_API_PASS", "lab123")
VERIFY = os.getenv("JUNOS_API_VERIFY", "false").lower() == "true"
OFFLINE = os.getenv("OFFLINE", "false").lower() in {"1", "true", "yes"}


def main() -> None:
    if OFFLINE:
        log.info("OFFLINE=1; reading Junos fixtures")
        with open("common/fixtures/junos_software_info.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))
        return

    if BASE.startswith("http"):
        with httpx.Client(verify=VERIFY, auth=(USER, PASS), timeout=10) as client:
            r = client.get(f"{BASE}get-software-information", headers={"Accept": "application/json"})
            log.info("GET software info: %s", r.status_code)
            print(json.dumps(r.json(), indent=2))
    else:
        with httpx.Client(timeout=10) as client:
            r = client.get("https://jsonplaceholder.typicode.com/users")
            log.info("GET mock users: %s", r.status_code)
            print(json.dumps(r.json()[:2], indent=2))


if __name__ == "__main__":
    main()
