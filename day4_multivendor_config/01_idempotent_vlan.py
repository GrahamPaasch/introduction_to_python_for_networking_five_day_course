"""Idempotent VLAN config via NAPALM where possible, or Netmiko templated CLI.
Dry-run capable and sandbox-safe by default (commit=False).
"""

import os
from typing import Dict

from napalm import get_network_driver  # type: ignore
from netmiko import ConnectHandler  # type: ignore

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("vlan-config")

TARGET_VLAN = int(os.getenv("TARGET_VLAN", "123"))
TARGET_NAME = os.getenv("TARGET_NAME", "TRAINING_VLAN")
COMMIT = os.getenv("COMMIT", "false").lower() == "true"


def configure_with_napalm(device, vlan_id: int, name: str) -> None:
    driver = get_network_driver(device.platform)
    dev = driver(hostname=device.host, username=device.username, password=device.password, optional_args={"port": device.port})
    dev.open()
    # Create candidate config idempotently
    if device.platform in ("ios", "iosxe", "nxos"):
        cfg = f"vlan {vlan_id}\n name {name}\n"
    elif device.platform == "junos":
        cfg = f"set vlans {name} vlan-id {vlan_id}\n"
    else:
        cfg = ""
    if cfg:
        dev.load_merge_candidate(config=cfg)
        diff = dev.compare_config()
        if diff:
            log.info("Diff for %s:\n%s", device.name, diff)
            if COMMIT:
                dev.commit_config()
            else:
                dev.discard_config()
        else:
            log.info("No changes for %s", device.name)
    dev.close()


def configure_with_netmiko(device, vlan_id: int, name: str) -> None:
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
            cmds = [f"vlan {vlan_id}", f"name {name}", "end", "write mem"]
        elif device.platform == "junos":
            cmds = [
                f"set vlans {name} vlan-id {vlan_id}",
                "commit confirmed 1",  # auto-rollback for safety
            ]
        else:
            cmds = []
        if cmds:
            if COMMIT:
                out = conn.send_config_set(cmds)
                log.info("Applied to %s: %s", device.name, out[:120])
            else:
                log.info("Dry-run for %s: %s", device.name, cmds)


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    for d in devices:
        try:
            configure_with_napalm(d, TARGET_VLAN, TARGET_NAME)
        except Exception as e:
            log.warning("NAPALM failed on %s: %s; trying Netmiko", d.name, e)
            configure_with_netmiko(d, TARGET_VLAN, TARGET_NAME)


if __name__ == "__main__":
    main()
