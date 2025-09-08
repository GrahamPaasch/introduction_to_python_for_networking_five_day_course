---
marp: true
title: Day 3 — API Errors, Pagination, Retries
paginate: true
---

# API Errors, Pagination, Retries

- Handling 4xx/5xx cleanly
- Backoff strategies
- Pagination patterns

---

## Errors

- Always `raise_for_status()`
- Parse error bodies for details
- Map to actionable logs

---

## Backoff

- Exponential (e.g., 0.5, 1, 2, 4s)
- Jitter to avoid thundering herd
- Max attempts and total time

---

## Pagination

- Link headers or `next` fields
- Accumulate pages with limits
- Validate item counts

---

## Rate Limiting

- Respect `Retry-After`
- Use request IDs in logs

