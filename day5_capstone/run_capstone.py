"""Capstone runner: inventory -> VLAN + interface desc + API query summary.
Dry-run by default.
"""

import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging
from common.lib.config_vlan import configure_with_napalm

log = setup_logging("capstone")

COMMIT = os.getenv("COMMIT", "false").lower() == "true"
TARGET_VLAN = int(os.getenv("TARGET_VLAN", "123"))
INT_DESC = os.getenv("INT_DESC", "Managed by Automation Training")


def do_vlan(device):
    # Use shared helper
    return configure_with_napalm(device, TARGET_VLAN, f"VLAN{TARGET_VLAN}")


def do_api_summary(device):
    # For Cisco IOS XE, pull RESTCONF interfaces; else mock
    return {"device": device.name, "api": "skipped-in-skeleton"}


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(do_vlan, d) for d in devices]
        for f in as_completed(futs):
            log.info("VLAN task done: %s", f.result())


if __name__ == "__main__":
    main()
