---
marp: true
title: Day 1 — Lab 1.2 Inventory Bootstrap
paginate: true
---

# Lab 1.2 — Inventory Bootstrap

- Build inventory from CSV/YAML → JSON
- Validate outputs
- Prep for Day 2 persistence

---

## Objectives

- Read sample CSV/YAML under `common/inventory/`
- Normalize fields (name, host, os, platform, port)
- Write `common/outputs/devices.json`

---

## Steps

1) Activate venv
2) Run `python day1_setup/06_inventory_bootstrap.py`
3) Inspect `common/outputs/devices.json`

---

## Validation

- `python -m json.tool common/outputs/devices.json`
- Ensure ≥ 2 devices
- Keys present: name, host, platform

---

## Stretch

- Add a device row to CSV; re‑run
- Change a port for a device; verify update

---

## What’s Next

- Persist to SQLite (Day 2)
- Use inventory across labs

