---
marp: true
title: Day 5 — Design Review & Guardrails
paginate: true
---

# Design Review & Guardrails

- Define change window & scope
- Failure modes & rollback
- Evidence artifacts

---

## Change Plan

- Goals and non‑goals
- Pre‑checks and success criteria
- Rollback or compensating actions

---

## Guardrails

- Dry‑run first everywhere
- Explicit `--apply` or `COMMIT=true`
- Per‑host isolation, timeouts, retries

---

## Evidence

- Logs with timestamps & request IDs
- Saved diffs and JSON outputs
- Post‑checks confirming no‑op on repeat

