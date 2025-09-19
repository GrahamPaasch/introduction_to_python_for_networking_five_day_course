"""Simple argparse demo: greet the user and echo a number.
"""

import argparse
from common.lib.logging_setup import setup_logging

log = setup_logging("cli-args")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("name", help="Your name")
    p.add_argument("--times", type=int, default=1, help="Repeat count")
    args = p.parse_args()
    for _ in range(max(1, args.times)):
        log.info("Hello, %s!", args.name)


if __name__ == "__main__":
    main()

