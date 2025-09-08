---
marp: true
title: Day 5 — Capstone Orchestration
paginate: true
---

# Capstone Orchestration

- Inventory → gather → API query → idempotent config → report
- Dry‑run default; explicit apply

---

## Components

- Inventory (`common/lib/inventory.py`)
- Gatherers (NAPALM/Netmiko/HTTP)
- Orchestrator (`day5_capstone/run_capstone.py`)

---

## Flags & Env

- `--dry-run` vs `--apply`
- `NET_USERNAME` / `NET_PASSWORD`
- `OFFLINE=1` for fixtures

---

## Outputs

- Per‑host logs
- Consolidated report (JSON/CSV)
- Saved diffs where applicable

---

## Demo Flow

1) Dry‑run end‑to‑end
2) Review evidence
3) Apply against sandbox

