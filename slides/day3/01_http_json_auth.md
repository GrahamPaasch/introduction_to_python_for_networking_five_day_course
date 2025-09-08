---
marp: true
title: Day 3 — HTTP, JSON, Auth
paginate: true
---

# HTTP, JSON, Auth

- HTTP verbs & status codes
- Headers & auth
- JSON payloads

---

## Verbs & Semantics

- GET — retrieve
- POST — create
- PUT/PATCH — replace/modify
- DELETE — remove

---

## Status Codes

- 2xx success, 4xx client, 5xx server
- 200/201/204 common
- 429 rate limit

---

## Headers

- `Accept: application/yang-data+json` (RESTCONF)
- `Content-Type: application/json`
- `X-HTTP-Method-Override` for dry‑run patterns

---

## Auth

- Basic auth for labs
- Tokens (bearer) in real‑world
- Never commit secrets

---

## Clients

- `requests` (sync)
- `httpx` (sync used here)
- Timeouts & retries mandatory

