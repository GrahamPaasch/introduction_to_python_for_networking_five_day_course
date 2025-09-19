"""Optional stretch lab: OSPF parameter update across platforms (dry-run by default).

This skeleton demonstrates generating simple OSPF config snippets per platform
and printing diffs/commands without applying changes. Intended for discussion
and exploration; adapt to your environment before applying.
"""

import os
from typing import Dict

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("ospf-optional")

AREA = os.getenv("OSPF_AREA", "0.0.0.0")
PROCESS_ID = os.getenv("OSPF_PROCESS", "1")
NETWORK = os.getenv("OSPF_NETWORK", "10.0.0.0 0.0.0.255")
IFACE = os.getenv("OSPF_IFACE", "GigabitEthernet1")


def render(platform: str) -> str:
    if platform in ("ios", "iosxe"):
        return (
            f"router ospf {PROCESS_ID}\n"
            f" network {NETWORK} area {AREA}\n"
        )
    if platform == "nxos":
        return (
            f"feature ospf\n"
            f"router ospf {PROCESS_ID}\n"
            f" interface {IFACE}\n ip router ospf {PROCESS_ID} area {AREA}\n"
        )
    if platform == "junos":
        return (
            f"set protocols ospf area {AREA} interface {IFACE}\n"
        )
    return ""


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    for d in devices:
        cfg = render(d.platform)
        if not cfg:
            log.info("Skipping %s (%s): platform unsupported for demo", d.name, d.platform)
            continue
        log.info("[DRY-RUN] OSPF config for %s (%s):\n%s", d.name, d.platform, cfg)


if __name__ == "__main__":
    main()

