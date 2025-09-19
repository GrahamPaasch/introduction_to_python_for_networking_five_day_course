# Day 04 — Multi‑Vendor Config & Ansible

## Learning outcomes
- Use Jinja2 templates for multi‑vendor config with validation.
- Execute idempotent changes and compare diffs.
- Understand core Ansible network workflows (inventory, vars, check mode, diffs).

## Materials & setup
- Slides (optional) — keep to <20 per day; demo beats slides.
- Whiteboard/markers for design discussions.
- Student repo cloned; `environment/bootstrap.sh` run; venv active.
- Access to `lab.grahampaasch.com`; GNS3 topology handy (see `docs/gns3.md`).

## Labs used today
- `labs/05_config_vlan` — Jinja2‑based multi‑vendor VLAN + descriptions (validate with NAPALM)
- `labs/06_ansible_intro` — reproduce 05 in Ansible with check mode + diffs

> **Schedule:** 8 x ~55‑min hours with two 10‑min breaks and a 45‑min lunch. Adjust to your start time.

## Hour‑by‑hour plan

### Hour 1: Templates, variables, and validation
- Jinja2 patterns; per‑vendor conditionals; pre/post checks with NAPALM.

### Hour 2: Lab 05 (part A) — render templates
- Generate configs for Cisco & Juniper; sanity check render.

### Hour 3: Lab 05 (part B) — apply + validate
- Push changes; collect diffs; verify via getters.

### Hour 4: Debrief + pitfalls
- Idempotence, ordering, partial failures, safe rollback.
- Short break (10 min) at end of hour.

### Hour 5: Ansible intro — the 90‑minute sprint
- Inventories/hosts, connection vars, network modules, check mode/diff.

### Hour 6: Lab 06 (part A) — translate Python flow to Ansible
- Reproduce VLAN change with check mode first.

### Hour 7: Lab 06 (part B) — diffs and evidence
- Capture diffs and post‑change validation outputs for report.

### Hour 8: Review + exit ticket
- Students submit rendered templates + Ansible diff evidence.
- Preview tomorrow: capstone (policy checks + change).
