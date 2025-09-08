---
marp: true
title: Day 2 — Validation Scripts & Reports
paginate: true
---

# Validation Scripts & Reports

- Scriptable checks with clear PASS/FAIL
- Exit codes + artifacts
- Simple reports

---

## Philosophy

- Fast, deterministic checks
- No external dependencies
- Summaries with counts

---

## Our Runner

- `scripts/run_validations.py`
- Defaults to `OFFLINE=1`
- Checks artifacts exist and exit code 0

---

## Adding a Check

- Append to `checks` list
- Provide artifact path if applicable

---

## Reports

- Generate CSV/JSON summaries
- Example: devices by OS, interface up/down

---

## Exercise

- Add a new validation for your custom script
- Print a one‑line summary per check

