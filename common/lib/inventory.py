import os
import json
from dataclasses import dataclass
from typing import List, Dict, Any

import yaml


@dataclass
class Device:
    name: str
    host: str
    os: str
    platform: str
    username: str
    password: str
    port: int = 22


class Inventory:
    def __init__(self, path: str):
        self.path = path
        self.devices: List[Device] = []

    def load(self) -> List[Device]:
        with open(self.path, "r", encoding="utf-8") as f:
            if self.path.endswith(".yaml") or self.path.endswith(".yml"):
                data = yaml.safe_load(f)
            elif self.path.endswith(".json"):
                data = json.load(f)
            else:
                raise ValueError("Unsupported inventory format")
        self.devices = [Device(**item) for item in data.get("devices", data)]
        # Env var overrides for secrets
        for d in self.devices:
            d.username = os.getenv("NET_USERNAME", d.username)
            d.password = os.getenv("NET_PASSWORD", d.password)
        return self.devices

    def to_json(self, out_path: str) -> None:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump([d.__dict__ for d in self.devices], f, indent=2)

    @staticmethod
    def example() -> Dict[str, Any]:
        return {
            "devices": [
                {
                    "name": "iosxe-sandbox",
                    "host": "sandbox-iosxe-latest-1.cisco.com",
                    "os": "cisco",
                    "platform": "iosxe",
                    "username": "developer",
                    "password": "C1sco12345",
                    "port": 22,
                },
                {
                    "name": "junos-vlabs",
                    "host": "xxxx.juniper.net",
                    "os": "juniper",
                    "platform": "junos",
                    "username": "lab",
                    "password": "lab123",
                    "port": 22,
                },
            ]
        }
