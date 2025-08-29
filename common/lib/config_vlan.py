"""Shared helpers for idempotent VLAN configuration using NAPALM.
Dry-run by default unless COMMIT=true in environment.
"""

import os
from typing import Any, Dict

from napalm import get_network_driver  # type: ignore

from .logging_setup import setup_logging

log = setup_logging("config-vlan")
COMMIT = os.getenv("COMMIT", "false").lower() == "true"


def configure_with_napalm(device, vlan_id: int, name: str) -> Dict[str, Any]:
    driver = get_network_driver(device.platform)
    dev = driver(
        hostname=device.host,
        username=device.username,
        password=device.password,
        optional_args={"port": device.port},
    )
    log.info("Connecting to %s for VLAN %s (%s)", device.name, vlan_id, name)
    dev.open()
    dev.load_merge_candidate(config=f"vlan {vlan_id}\n name {name}\n")
    diff = dev.compare_config()
    result: Dict[str, Any] = {"device": device.name, "diff": diff}
    if diff and COMMIT:
        dev.commit_config()
        result["committed"] = True
    else:
        dev.discard_config()
        result["committed"] = False
    dev.close()
    return result
