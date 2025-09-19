---
marp: true
title: Day 2 — Lab 2.2 Inventory Persistence
paginate: true
---

# Lab 2.2 — Inventory Persistence

- YAML/CSV → JSON + SQLite
- Validation scripts

---

## Objectives

- Use `Inventory` to load YAML/CSV
- Write `common/outputs/devices.json`
- Upsert into `common/outputs/inventory.sqlite`

---

## Steps

1) Run `python day2_cli_to_data/00_inventory_persist.py`
2) Query SQLite: list devices per OS
3) Add one device, re‑run, verify upsert

---

## Validation

- `sqlite-utils tables common/outputs/inventory.sqlite`
- Row count ≥ 2

---

## Stretch

- Add index on `name`
- Export report as CSV

