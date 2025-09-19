"""Collect show output via Netmiko and parse to JSON.
Safe for sandboxes; read-only commands only.
"""

import os
from typing import Any, Dict
from netmiko import ConnectHandler
from common.lib.logging_setup import setup_logging
from common.lib.inventory import Inventory

log = setup_logging("netmiko-show")


SHOW_CMDS = {
    "iosxe": ["show version", "show ip interface brief"],
    "nxos": ["show version", "show interface brief"],
    "junos": ["show version | display json", "show interfaces terse | display json"],
    # Firewalls (examples): ASA supports cisco_asa driver
    "cisco_asa": ["show version", "show interface ip brief"],
}


def run() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    for d in devices:
        driver: Dict[str, Any] = {
            "device_type": f"{d.platform}",
            "host": d.host,
            "username": d.username,
            "password": d.password,
            "port": d.port,
            "fast_cli": True,
        }
        secret = os.getenv("NET_SECRET")
        if secret:
            driver["secret"] = secret
        log.info("Connecting to %s (%s)", d.name, d.platform)
        with ConnectHandler(**driver) as conn:
            try:
                if secret:
                    conn.enable()
            except Exception:
                pass
            for cmd in SHOW_CMDS.get(d.platform, ["show version"]):
                out = conn.send_command(cmd, use_textfsm=True)
                log.info("%s => %s", cmd, type(out))
                print({"device": d.name, "cmd": cmd, "result": out})


if __name__ == "__main__":
    run()
