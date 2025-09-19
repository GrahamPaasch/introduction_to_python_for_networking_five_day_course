"""Convert YAML inventory to JSON and SQLite."""

from common.lib.inventory import Inventory
from common.lib.db import upsert_devices


def main() -> None:
    inv = Inventory("common/inventory/devices.yaml")
    devices = inv.load()
    inv.to_json("common/outputs/devices.json")
    upsert_devices([d.__dict__ for d in devices])


if __name__ == "__main__":
    main()
