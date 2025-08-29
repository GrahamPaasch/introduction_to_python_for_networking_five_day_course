"""Cisco IOS XE RESTCONF examples using requests.
Switch to mocks (httpbin/jsonplaceholder) if env vars not set.
"""

import os
import json
from typing import Dict

import requests

from common.lib.logging_setup import setup_logging

log = setup_logging("restconf")

BASE = os.getenv("RESTCONF_BASE", "")  # e.g., https://sandbox-iosxe-latest-1.cisco.com:443/restconf
USER = os.getenv("RESTCONF_USER", "developer")
PASS = os.getenv("RESTCONF_PASS", "C1sco12345")
VERIFY = os.getenv("RESTCONF_VERIFY", "false").lower() == "true"


HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def restconf_enabled() -> bool:
    return BASE.startswith("http") and "restconf" in BASE


def get_session() -> requests.Session:
    s = requests.Session()
    s.auth = (USER, PASS)
    s.verify = VERIFY
    s.headers.update(HEADERS)
    return s


def main() -> None:
    s = get_session()

    if restconf_enabled():
        # GET hostname (ietf-interfaces as a harmless read)
        url = f"{BASE}/data/ietf-interfaces:interfaces"
        r = s.get(url, timeout=10)
        log.info("GET interfaces status=%s", r.status_code)
        print(json.dumps(r.json(), indent=2))
    else:
        # Fallback to httpbin/jsonplaceholder mocks
        r = s.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
        log.info("GET mock status=%s", r.status_code)
        todo: Dict = r.json()
        print(json.dumps(todo, indent=2))

        # POST mock
        r2 = s.post("https://httpbin.org/post", json={"vlan": 10, "name": "US-East"}, timeout=10)
        log.info("POST mock status=%s", r2.status_code)
        print(r2.json()["json"])

    # PUT mock
    r3 = s.put("https://httpbin.org/put", json={"vlan": 10, "name": "US-East-Updated"}, timeout=10)
    log.info("PUT mock status=%s", r3.status_code)
    print(r3.json()["json"])

    # DELETE mock
    r4 = s.delete("https://httpbin.org/delete", timeout=10)
    log.info("DELETE mock status=%s", r4.status_code)


if __name__ == "__main__":
    main()
