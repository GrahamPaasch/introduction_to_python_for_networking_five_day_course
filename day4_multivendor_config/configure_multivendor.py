"""Orchestrate multi-vendor idempotent config: VLAN + interface descriptions.
Dry-run by default; set COMMIT=true to apply. Uses NAPALM where possible.
"""

import os
from typing import Dict

from netmiko import ConnectHandler  # type: ignore
from napalm import get_network_driver  # type: ignore

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("multivendor-config")

VLAN_ID = int(os.getenv("TARGET_VLAN", "123"))
VLAN_NAME = os.getenv("TARGET_NAME", "TRAINING_VLAN")
IFACE = os.getenv("IFACE", "GigabitEthernet1")
DESC = os.getenv("DESC", "Managed by Automation Training")
COMMIT = os.getenv("COMMIT", "false").lower() == "true"


def vlan_with_napalm(device) -> None:
    driver = get_network_driver(device.platform)
    dev = driver(
        hostname=device.host,
        username=device.username,
        password=device.password,
        optional_args={"port": device.port},
    )
    dev.open()
    if device.platform in ("ios", "iosxe", "nxos"):
        cfg = f"vlan {VLAN_ID}\n name {VLAN_NAME}\n"
    elif device.platform == "junos":
        cfg = f"set vlans {VLAN_NAME} vlan-id {VLAN_ID}\n"
    else:
        cfg = ""
    if cfg:
        dev.load_merge_candidate(config=cfg)
        diff = dev.compare_config()
        if diff:
            log.info("VLAN diff on %s:\n%s", device.name, diff)
            if COMMIT:
                dev.commit_config()
            else:
                dev.discard_config()
        else:
            log.info("VLAN: no changes for %s", device.name)
    dev.close()


def iface_desc_with_netmiko(device) -> None:
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
            # Map a common iface name to Junos demo default
            cmds = [f"set interfaces ge-0/0/0 description \"{DESC}\"", "commit confirmed 1"]
        else:
            cmds = []
        if not cmds:
            return
        if COMMIT:
            out = conn.send_config_set(cmds)
            log.info("Iface desc applied on %s: %s", device.name, out[:120])
        else:
            log.info("Iface desc dry-run on %s: %s", device.name, cmds)


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    for d in devices:
        try:
            vlan_with_napalm(d)
        except Exception as e:
            log.warning("NAPALM VLAN failed on %s: %s; skipping VLAN", d.name, e)
        try:
            iface_desc_with_netmiko(d)
        except Exception as e:
            log.warning("Iface desc failed on %s: %s", d.name, e)


if __name__ == "__main__":
    main()

