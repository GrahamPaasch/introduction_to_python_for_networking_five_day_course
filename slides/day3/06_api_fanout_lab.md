---
marp: true
title: Day 3 — Lab 3.3 API Fan‑Out
paginate: true
---

# Lab 3.3 — API Fan‑Out

- Parallel API requests
- Timeouts, retries, backoff
- Summaries and logs

---

## Objectives

- Use ThreadPool to query many endpoints
- Handle failures per‑host cleanly
- Collect structured results

---

## Steps

1) Implement worker with timeout + retry
2) Submit tasks for each host
3) Aggregate results; write JSON

---

## Validation

- Logs show request IDs per host
- Summary: success/fail counts and timings

---

## Stretch

- Add rate‑limit handling (429)
- Record per‑host latency histogram

