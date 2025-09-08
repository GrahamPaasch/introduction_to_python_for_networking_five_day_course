---
marp: true
title: Day 4 — Lab 4.1 Threaded Gather with Retries
paginate: true
---

# Lab 4.1 — Threaded Gather with Retries

- Combine Netmiko and NAPALM collectors
- Run in parallel with robust error handling

---

## Objectives

- Implement per‑task retries with backoff
- Collect structured results per host
- Summarize failures without crashing

---

## Steps

1) Create worker for CLI + getter
2) Submit via ThreadPool (bounded)
3) Aggregate JSON outputs

---

## Validation

- Logs show retry attempts & timings
- Summary counts at end

---

## Stretch

- Add per‑host timeouts
- Export metrics (CSV)

