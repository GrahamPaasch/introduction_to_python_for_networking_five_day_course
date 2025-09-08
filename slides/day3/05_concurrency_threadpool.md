---
marp: true
title: Day 3 — Concurrency (ThreadPoolExecutor)
paginate: true
---

# Concurrency — ThreadPoolExecutor

- When to parallelize
- Thread pools for I/O
- Timeouts and per‑task retries

---

## ThreadPool Basics

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=10) as ex:
    futs = {ex.submit(do_work, d): d for d in devices}
    for fut in as_completed(futs):
        handle(fut.result())
```

---

## Patterns

- Bound workers to avoid overload
- Per‑future exception handling
- Summaries at completion

---

## Lab Tie‑In

- Used in HTTP fan‑out (Lab 3.3)
- Also used Day 4 threaded gather

