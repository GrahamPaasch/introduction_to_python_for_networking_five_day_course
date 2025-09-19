# Day 01 — Foundations & Device Access

## Learning outcomes
- Orient students to modern NetOps use‑cases and the course flow.
- Ensure all students can run code locally (venv) and access devices.
- Build a clean inventory (CSV/YAML → JSON/SQLite).
- Establish safe device connectivity patterns with Netmiko.

## Materials & setup
- Slides (optional) — keep to <20 per day; demo beats slides.
- Whiteboard/markers for design discussions.
- Student repo cloned; `environment/bootstrap.sh` run; venv active.
- Access to `lab.grahampaasch.com`; GNS3 topology handy (see `docs/gns3.md`).

## Labs used today
- `labs/01_inventory` — inventory to JSON/SQLite
- `labs/02_connectivity` — safe CLI execution with Netmiko (offline fixtures available)

> **Schedule:** 8 x ~55‑min hours with two 10‑min breaks and a 45‑min lunch. Adjust to your start time.

## Hour‑by‑hour plan

### Hour 1: Kickoff, outcomes, lab portal check
- Set expectations; show the campus diagram (docs/gns3.md).
- Live demo: log into `lab.grahampaasch.com`.
- Students: clone repo; run `environment/bootstrap.sh`.
- Done when: everyone activates `.venv` and passes the import smoke.

### Hour 2: Python essentials (functions, exceptions, logging)
- Quick warm‑ups: parse JSON, write a small function with error handling.
- Instructor demo: `logging` basics for network scripts.
- Short break (10 min) at end of hour.

### Hour 3: Lab 01 — Inventory (part A)
- Read `devices.csv` / `devices.yaml`.
- Normalize records; write to `expected_output/inventory.json`.
- Stretch: also persist to `inventory.sqlite` (table: devices).

### Hour 4: Debrief + Lab 01 (part B)
- Walk through solution; highlight CSV vs YAML tradeoffs.
- Add validation (required fields, IP format).

### Hour 5: Safe device access patterns
- Explain prompts/privilege and timing concerns.
- Introduce Netmiko connection params; `.enable()` usage.
- Show vendor‑specific show commands map.

### Hour 6: Lab 02 — Connectivity (part A)
- Run with `--offline` first; verify file outputs per host.
- Then attempt real device exec on at least one Cisco box.

### Hour 7: Lab 02 — Connectivity (part B) + error handling
- Add retries/backoff; collect failures in a report.

### Hour 8: Review + exit ticket
- Students submit inventory JSON and one real CLI capture.
- Preview tomorrow: SNMP & syslog parsing.

## Plan‑B (offline)
- Use `labs/02_connectivity/fixtures/*.txt` when devices are busy.
- Pair‑program students lacking access; instructor runs live demo captures.

## Assessment / Exit ticket
- Inventory JSON/SQLite present and valid.
- At least one CLI output file produced (offline or real).

## Homework / Prep for tomorrow
- Optional reading: quick Python recap (functions/files/JSON).
- Skim SNMP/syslog primer (provided links in class LMS).
