---
marp: true
title: Day 2 — Lab 2.1 NAPALM Getters
paginate: true
---

# Lab 2.1 — NAPALM Getters

- Collect facts, interfaces, routes
- Offline‑first using fixtures

---

## Objectives

- Use NAPALM drivers per platform
- Persist results to JSON
- Summarize counts

---

## Steps

1) `OFFLINE=1 python day2_cli_to_data/02_napalm_getters.py`
2) Inspect `common/outputs/napalm_results.json`
3) Count interfaces per device

---

## Validation

- JSON exists and non‑empty
- Script exit code 0

---

## Troubleshooting

- Driver mismatch → check `platform`
- Offline mode not set → network errors

