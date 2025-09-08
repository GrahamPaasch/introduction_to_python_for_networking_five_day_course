---
marp: true
title: Day 2 — SQLite Basics
paginate: true
---

# SQLite Basics

- Why SQLite for labs
- Tables & simple queries
- Writing via Python

---

## Why SQLite

- Zero‑config, file‑based DB
- Easy to share and validate
- Good enough for reports

---

## Python API

- `sqlite3.connect('inventory.db')`
- `cur.execute('CREATE TABLE IF NOT EXISTS ...')`
- `INSERT OR REPLACE` for upserts

---

## Our Helper

- `common/lib/db.py` provides `upsert_devices`
- Used in `day2_cli_to_data/00_inventory_persist.py`

---

## Queries

- Devices by OS
- Count interfaces by status (from getters)

---

## Exercise

- Add a query that lists device names per platform
- Print results as CSV

