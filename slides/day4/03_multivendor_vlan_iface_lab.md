---
marp: true
title: Day 4 — Lab 4.2 Multi‑Vendor VLAN + Interface
paginate: true
---

# Lab 4.2 — Multi‑Vendor VLAN + Interface

- VLAN creation/update (IOS XE/NX‑OS/Junos)
- Interface description updates
- Idempotence via pre/post checks

---

## Objectives

- Render VLAN config via Jinja2
- Apply via NAPALM merge candidate
- Update interface description via Netmiko

---

## Steps

1) Dry‑run: `python day4_multivendor_config/configure_multivendor.py`
2) Review diffs in logs
3) Apply: `COMMIT=true python ...`
4) Re‑run to confirm no‑op

---

## Validation

- First run shows diffs/changes
- Second run shows “no changes”

---

## Troubleshooting

- Platform mismatches → check inventory
- Auth/ports → env vars

