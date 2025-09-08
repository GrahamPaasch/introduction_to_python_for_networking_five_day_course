---
marp: true
title: Day 3 — Cisco RESTCONF
paginate: true
---

# Cisco RESTCONF

- Endpoints & YANG resources
- GET/PUT patterns
- Fixture‑backed offline mode

---

## Endpoints

- Base: `/restconf/data/` (IOS XE sandbox)
- Example: interfaces `ietf-interfaces:interfaces/interface`

---

## GET Example

```python
resp = s.get(url, headers=hdrs, timeout=5)
resp.raise_for_status()
data = resp.json()
```

---

## PUT (Idempotent)

- Replace or create resource
- Validate first → compare
- Apply only on change

---

## Offline Mode

- `OFFLINE=1 python day3_rest_and_json/01_restconf_requests.py`
- Reads `common/fixtures/mock_restconf_interfaces.json`

---

## Validation

- Save responses to JSON files
- Log request IDs + timing

