---
marp: true
title: Day 4 — Config Diff Demo
paginate: true
---

# Config Diff Demo (Stdlib)

- Show changes clearly
- Teach idempotence visually

---

## Files

- `common/fixtures/config_before.txt`
- `common/fixtures/config_after.txt`

---

## difflib

```python
from difflib import unified_diff

diff = unified_diff(
  before.splitlines(), after.splitlines(),
  fromfile='before', tofile='after')
print('\n'.join(diff))
```

---

## Demo Steps

1) Run `python day4_multivendor_config/04_config_diff_demo.py`
2) Discuss insertions/deletions
3) Tie to idempotent apply

