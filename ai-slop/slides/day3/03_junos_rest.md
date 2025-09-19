---
marp: true
title: Day 3 — Junos REST
paginate: true
---

# Junos REST

- GET/POST/DELETE
- Validate‑only strategies
- Fixture‑backed offline mode

---

## Endpoints

- Base: `/rpc/` or `/rest/` depending on mode
- We use simplified HTTPX client

---

## GET Example

```python
resp = client.get(url, headers=h, timeout=5)
data = resp.json()
```

---

## Validate‑Only Pattern

- Dry‑run equivalent where supported
- Compare state → act only on diff

---

## Offline Mode

- `OFFLINE=1 python day3_rest_and_json/02_junos_rest_httpx.py`
- Reads `common/fixtures/junos_software_info.json`

---

## Validation

- Log summaries; store JSON

