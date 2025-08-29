"""Standardize interface description in an idempotent manner using Netmiko.
Dry-run by default unless COMMIT=true.
"""

import os
from typing import Dict

from netmiko import ConnectHandler  # type: ignore

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("int-desc")
COMMIT = os.getenv("COMMIT", "false").lower() == "true"
IFACE = os.getenv("IFACE", "GigabitEthernet1")
DESC = os.getenv("DESC", "Managed by Automation Training")


def apply_desc(device) -> None:
    params: Dict = {
        "device_type": device.platform,
        "host": device.host,
        "username": device.username,
        "password": device.password,
        "port": device.port,
        "fast_cli": True,
    }
    with ConnectHandler(**params) as conn:
        if device.platform in ("ios", "iosxe", "nxos"):
            cmds = [f"interface {IFACE}", f"description {DESC}", "end", "write mem"]
        elif device.platform == "junos":
            cmds = [f"set interfaces ge-0/0/0 description \"{DESC}\"", "commit confirmed 1"]
        else:
            cmds = []
        if cmds:
            if COMMIT:
                out = conn.send_config_set(cmds)
                log.info("Applied to %s: %s", device.name, out[:120])
            else:
                log.info("Dry-run for %s: %s", device.name, cmds)


if __name__ == "__main__":
    inv = Inventory("common/inventory/devices.yaml")
    for d in inv.load():
        apply_desc(d)
