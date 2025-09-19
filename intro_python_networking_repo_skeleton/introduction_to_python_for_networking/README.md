# Introduction to Python for Networking — Teacher Repo

**Goal:** a teacher-first, runnable set of labs for a 5‑day course covering inventory, connectivity, SNMP/syslog parsing, REST APIs, multi‑vendor configuration, and an Ansible intro.

## Quick start (60 seconds)

```bash
cd introduction_to_python_for_networking/environment
bash bootstrap.sh
# Then run labs:
cd ../labs/01_inventory && python starter.py
```

## Repo map

- `COURSE_PLAN.md` — 5‑day schedule & outcomes
- `PREWORK.md` — accounts, VS Code + Python, lab access
- `environment/` — pinned deps and one-shot setup script
- `labs/` — student labs with starter code, solutions, expected outputs
- `solutions/` — instructor reference solutions (mirrors labs)
- `ansible/` — inventories/playbooks for the Ansible lab
- `ci/` — pre-commit config; GitHub Actions smoke workflow

> **Note:** Use the fixtures in SNMP/syslog labs to run fully offline if the simulator is busy.
