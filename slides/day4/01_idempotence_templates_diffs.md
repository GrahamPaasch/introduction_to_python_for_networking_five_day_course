---
marp: true
title: Day 4 — Idempotence, Templates, Diffs
paginate: true
---

# Idempotence, Templates, Diffs

- Make changes only when needed
- Render config with Jinja2
- Show and store diffs

---

## Idempotence

- Pre‑check → Decide → Apply → Post‑check
- Second run is a no‑op
- Evidence artifacts (logs + diffs)

---

## Templates (Jinja2)

- `common/templates/ios_vlan.j2`
- `common/templates/junos_vlan.set.j2`
- Render with platform‑specific templates

---

## Orchestrator

- `day4_multivendor_config/configure_multivendor.py`
- NAPALM merge candidate for VLAN
- Netmiko for interface descriptions

---

## Diffs

- NAPALM `compare_config()`
- Stdlib `difflib.unified_diff`
- Store in logs or files

---

## Safety

- Dry‑run by default (`COMMIT=true` to apply)
- Env secrets; per‑host error isolation

