# Day 05 — Capstone & Demos

## Learning outcomes
- Design and execute an end‑to‑end change with guardrails.
- Collect evidence (diffs, validation) and present a brief demo/readout.

## Materials & setup
- Slides (optional) — keep to <20 per day; demo beats slides.
- Whiteboard/markers for design discussions.
- Student repo cloned; `environment/bootstrap.sh` run; venv active.
- Access to `lab.grahampaasch.com`; GNS3 topology handy (see `docs/gns3.md`).

## Labs used today
- `labs/` — use prior pieces to build a mini‑pipeline (inventory → checks → change → evidence)

> **Schedule:** 8 x ~55‑min hours with two 10‑min breaks and a 45‑min lunch. Adjust to your start time.

## Hour‑by‑hour plan

### Hour 1: Capstone briefing & team formation
- Pick a realistic change (VLAN add, interface desc cleanup, minor OSPF param).
- Define success criteria and rollback.

### Hour 2: Plan & stub
- Write plan; outline pre/post checks; assign roles.

### Hour 3: Build
- Implement inventory read + state collection; implement checks.

### Hour 4: Change path & validation
- Render/apply change; validate via getters; capture diffs.
- Lunch (45 min) around here.

### Hour 5: Harden & document
- Handle expected errors; make outputs reproducible (JSON/markdown evidence).

### Hour 6: Dry run
- Run end‑to‑end once on a small scope; finalize evidence bundle.

### Hour 7: Demos
- Each team presents 5–7 minutes; Q&A.

### Hour 8: Retrospective & next steps
- What worked, what to improve; map to client outcomes; share repos.

## Assessment / Exit ticket
- Team demo and an evidence bundle: pre/post checks, diffs, and a short readme.
