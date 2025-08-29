"""Inventory to NAPALM getters, store results in SQLite and JSON."""

import json
from typing import Any, Dict

from napalm import get_network_driver  # type: ignore

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging
from common.lib.db import upsert_devices

log = setup_logging("napalm-getters")


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()

    # persist inventory structure to db
    upsert_devices([d.__dict__ for d in devices])

    results: Dict[str, Dict[str, Any]] = {}
    for d in devices:
        driver = get_network_driver(d.platform)
        dev = driver(hostname=d.host, username=d.username, password=d.password, optional_args={"port": d.port})
        log.info("Opening NAPALM connection to %s", d.name)
        dev.open()
        facts = dev.get_facts()
        interfaces = dev.get_interfaces()
        results[d.name] = {"facts": facts, "interfaces": interfaces}
        dev.close()

    with open("common/outputs/napalm_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
