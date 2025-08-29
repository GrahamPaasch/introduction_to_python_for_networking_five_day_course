"""Quick environment check script."""

import os
import sys

import requests  # type: ignore
import httpx  # type: ignore

from common.lib.logging_setup import setup_logging

log = setup_logging("envcheck")


def main() -> int:
    log.info("Python version: %s", sys.version)
    log.info("Requests: %s", requests.__version__)
    log.info("HTTPX: %s", httpx.__version__)

    # Proxy awareness
    for key in ["HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY"]:
        if os.getenv(key) or os.getenv(key.lower()):
            log.info("Env %s is set", key)

    # Simple GET to a public mock
    try:
        r = requests.get("https://httpbin.org/get", timeout=5)
        r.raise_for_status()
        log.info("HTTP GET ok: %s", r.json().get("url"))
    except Exception as e:
        log.warning("HTTP GET failed: %s", e)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
