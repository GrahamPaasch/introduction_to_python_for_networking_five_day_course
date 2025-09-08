"""Orchestrate multi-vendor idempotent config: VLAN + interface descriptions.
Dry-run by default; set COMMIT=true to apply.

Enhancement: Uses Jinja2 templates for VLAN configuration when available,
falling back to inline strings. NAPALM applies merge candidates for safety.
"""

import os
from typing import Dict

from netmiko import ConnectHandler  # type: ignore
from napalm import get_network_driver  # type: ignore

try:
    from jinja2 import Environment, FileSystemLoader  # type: ignore

    JINJA = Environment(loader=FileSystemLoader("common/templates"))
except Exception:  # Jinja2 optional
    JINJA = None

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("multivendor-config")

VLAN_ID = int(os.getenv("TARGET_VLAN", "123"))
VLAN_NAME = os.getenv("TARGET_NAME", "TRAINING_VLAN")
IFACE = os.getenv("IFACE", "GigabitEthernet1")
DESC = os.getenv("DESC", "Managed by Automation Training")
COMMIT = os.getenv("COMMIT", "false").lower() == "true"


def render_vlan_config(platform: str, vlan_id: int, vlan_name: str) -> str:
    """Render VLAN config via Jinja2 when templates exist; fallback to f-strings."""
    if JINJA:
        try:
            if platform in ("ios", "iosxe", "nxos"):
                tpl = JINJA.get_template("ios_vlan.j2")
            elif platform == "junos":
                tpl = JINJA.get_template("junos_vlan.set.j2")
            else:
                tpl = None
            if tpl:
                return tpl.render(vlan_id=vlan_id, vlan_name=vlan_name)
        except Exception:
            # fall back below on any template issue
            pass

    if platform in ("ios", "iosxe", "nxos"):
        return f"vlan {vlan_id}\n name {vlan_name}\n"
    if platform == "junos":
        return f"set vlans {vlan_name} vlan-id {vlan_id}\n"
    return ""


def vlan_with_napalm(device) -> None:
    driver = get_network_driver(device.platform)
    dev = driver(
        hostname=device.host,
        username=device.username,
        password=device.password,
        optional_args={"port": device.port},
    )
    dev.open()
    cfg = render_vlan_config(device.platform, VLAN_ID, VLAN_NAME)
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
