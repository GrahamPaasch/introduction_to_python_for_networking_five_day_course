"""Convert CSV inventory to YAML for students preferring spreadsheets."""

import csv
import sys
import yaml  # type: ignore


def main(csv_path: str, yaml_path: str) -> None:
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    data = {"devices": rows}
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day2_cli_to_data/03_csv_to_yaml.py input.csv output.yaml")
        raise SystemExit(2)
    main(sys.argv[1], sys.argv[2])
