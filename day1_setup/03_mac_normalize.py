"""Normalize MAC addresses to aa:bb:cc:dd:ee:ff format.
Beginner-friendly: regex + string ops; optional CLI arg.
"""

import re
import sys
from typing import List

from common.lib.logging_setup import setup_logging

log = setup_logging("mac-normalize")

MAC_RE = re.compile(r"(?i)([0-9a-f]{2})[:\-\. ]?([0-9a-f]{2})[:\-\. ]?([0-9a-f]{2})[:\-\. ]?([0-9a-f]{2})[:\-\. ]?([0-9a-f]{2})[:\-\. ]?([0-9a-f]{2})")


def normalize(mac: str) -> str:
    m = MAC_RE.search(mac)
    if not m:
        raise ValueError(f"invalid MAC: {mac}")
    parts = [p.lower() for p in m.groups()]
    return ":".join(parts)


def demo() -> None:
    samples: List[str] = [
        "AA:BB:CC:DD:EE:FF",
        "aabb.ccdd.eeff",
        "aa-bb-cc-dd-ee-ff",
        "aa bb cc dd ee ff",
    ]
    for s in samples:
        log.info("%s -> %s", s, normalize(s))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(normalize(sys.argv[1]))
    else:
        demo()

