"""Run commands across N devices with ThreadPoolExecutor with timeouts and retries."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any
import time

from netmiko import ConnectHandler  # type: ignore

from common.lib.inventory import Inventory
from common.lib.logging_setup import setup_logging

log = setup_logging("fanout")

CMD = "show version"
TIMEOUT_S = 12
RETRIES = 2


def run_cmd(dev) -> Dict[str, Any]:
    for attempt in range(1, RETRIES + 1):
        try:
            with ConnectHandler(
                device_type=dev.platform,
                host=dev.host,
                username=dev.username,
                password=dev.password,
                port=dev.port,
                fast_cli=True,
                timeout=TIMEOUT_S,
            ) as conn:
                out = conn.send_command(CMD)
                return {"device": dev.name, "ok": True, "out": out[:120]}
        except Exception as e:
            log.warning("%s attempt %s failed: %s", dev.name, attempt, e)
            time.sleep(1 * attempt)  # backoff
    return {"device": dev.name, "ok": False, "error": f"failed after {RETRIES} retries"}


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    with ThreadPoolExecutor(max_workers=min(8, len(devices) or 1)) as ex:
        futures = [ex.submit(run_cmd, d) for d in devices]
        for fut in as_completed(futures):
            log.info("%s", fut.result())


if __name__ == "__main__":
    main()
