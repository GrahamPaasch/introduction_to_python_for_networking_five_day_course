---
marp: true
title: Day 2 — Data Structures & Parsing
paginate: true
---

# Data Structures & Parsing

- CSV / JSON / YAML
- Normalization patterns
- Safe parsing tips

---

## CSV

- `csv.DictReader`
- Convert numeric strings (e.g., port) to int
- Trim/normalize headers

---

## JSON

- `json.load()` / `json.dump(..., indent=2)`
- Schema stability across labs
- Validate with `python -m json.tool`

---

## YAML

- `yaml.safe_load()`
- Beware of implicit types; cast explicitly
- Example inventory YAML → list of devices

---

## Normalization

- Consistent keys: `name, host, os, platform, port`
- Defaults: `port=22`
- Env var overrides for secrets

---

## Practice

- Convert CSV → YAML: `day2_cli_to_data/03_csv_to_yaml.py`
- Validate fields and types

