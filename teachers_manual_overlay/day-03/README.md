# Day 03 — RESTful APIs for Network Automation

## Learning outcomes
- Apply REST fundamentals: auth, status codes, pagination, retries.
- Perform GET/PUT/PATCH/DELETE against Cisco RESTCONF and/or Junos REST.
- Design idempotent update patterns with validation/rollback.

## Materials & setup
- Slides (optional) — keep to <20 per day; demo beats slides.
- Whiteboard/markers for design discussions.
- Student repo cloned; `environment/bootstrap.sh` run; venv active.
- Access to `lab.grahampaasch.com`; GNS3 topology handy (see `docs/gns3.md`).

## Labs used today
- `labs/04_rest_apis` — RESTCONF/Junos REST with fixtures for offline safety

> **Schedule:** 8 x ~55‑min hours with two 10‑min breaks and a 45‑min lunch. Adjust to your start time.

## Hour‑by‑hour plan

### Hour 1: REST fundamentals for NetOps
- Status codes, verbs, headers, JSON shapes, backoff strategies.

### Hour 2: Auth flows + tooling
- Environment handling for tokens; Postman vs Python; requests/httpx.
- Short break (10 min) at end of hour.

### Hour 3: Lab 04 (part A) — GET inventory/state
- Pull interfaces/VLANs; print concise summaries.

### Hour 4: Lab 04 (part B) — PUT/PATCH change + validate
- Apply a small change; verify via GET; handle errors cleanly.

### Hour 5: Rollback design
- Design pre‑checks, post‑checks, and a revert path.

### Hour 6: Lab 04 (part C) — add retries/backoff
- Handle 429/5xx with exponential backoff and idempotency keys.

### Hour 7: Debrief + API diffs vs CLI diffs
- Show tradeoffs; where API wins; where CLI is still needed.

### Hour 8: Review + exit ticket
- Students submit a transcript of one successful GET and one change with validation.
- Preview tomorrow: config at scale with templates + Ansible.
