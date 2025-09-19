#!/usr/bin/env bash
set -euo pipefail

mkdir -p assets/gns3
mkdir -p day01_foundations_connectivity/labs/01_inventory/{starter,expected_output}
mkdir -p day01_foundations_connectivity/labs/02_connectivity/{starter,expected_output}
mkdir -p day02_snmp_syslog/labs/03_parse_snmp_syslog/{starter,expected_output}
mkdir -p day03_rest_apis/labs/04_rest_apis/{starter,expected_output}
mkdir -p day04_config_and_ansible/labs/05_config_vlan/{starter,expected_output}
mkdir -p day04_config_and_ansible/labs/06_ansible_intro/{starter,expected_output}
mkdir -p day05_capstone
mkdir -p environment

cat <<'DOC' > README.md
# Introduction to Python for Networking — Teacher Manual

This repository provides a day-by-day instructor manual for a five-day networking automation course. Quick start: clone the repo on a clean machine, run `bash environment/bootstrap.sh` to prep the virtual environment, and follow the daily links in `SCHEDULE.md`.
DOC

cat <<'DOC' > SCHEDULE.md
# Course Schedule

- [Day 1: Foundations & Connectivity](day01_foundations_connectivity/)
- [Day 2: SNMP & Syslog Automation](day02_snmp_syslog/)
- [Day 3: REST APIs & Orchestration](day03_rest_apis/)
- [Day 4: Configuration & Ansible](day04_config_and_ansible/)
- [Day 5: Capstone Integration](day05_capstone/)
- [Shared Assets (GNS3)](assets/gns3/)
DOC

cat <<'DOC' > PREWORK.md
# Prework

1. Install GNS3 or confirm access to the shared GNS3 server; download the current project bundle. [TODO: Provide GNS3 project link.]
2. Ensure Python 3.10+ and Git are available on your workstation; macOS/Linux recommended.
3. Clone the repository and run `bash environment/bootstrap.sh` to create the course virtual environment ahead of time.
4. Review `assets/gns3/topology-diagram.png` and `assets/gns3/login-table.md` so you recognize device roles before Day 1.
5. Verify you can reach the offline fixture share for inventory, connectivity, SNMP, syslog, REST, and Ansible labs. [TODO: Insert fixture share path.]
DOC

cat <<'DOC' > assets/gns3/login-table.md
# GNS3 Login Reference

| Device | Role | Management IP | Username | Password |
| --- | --- | --- | --- | --- |
| r1 | Edge router | [TODO: IP] | [TODO: user] | [TODO: password] |
| sw1 | Distribution switch | [TODO: IP] | [TODO: user] | [TODO: password] |
| srv-python | Automation jump host | [TODO: IP] | [TODO: user] | [TODO: password] |
DOC

cat <<'DOC' > assets/gns3/topology-diagram.png
Placeholder: replace this file with the latest GNS3 topology diagram screenshot before teaching. [TODO: Export PNG from GNS3.]
DOC

cat <<'DOC' > day01_foundations_connectivity/INSTRUCTOR.md
# Day 1 Instructor Guide — Foundations & Connectivity

## Objectives
- Align the cohort on the modern NetOps roadmap and course expectations.
- Demonstrate gathering inventory data with Python before touching production devices.
- Validate reachability using offline fixtures so students can compare with lab equipment.

## Prep
- Review `day01_foundations_connectivity/labs/01_inventory/starter` fixtures and update hostnames, IPs, and device roles. [TODO: Confirm device list for this cohort.]
- Refresh the GNS3 project and verify screenshots in `assets/gns3/` reflect the current topology.
- Run `bash environment/bootstrap.sh` to rebuild the virtual environment and smoke-test imports.
- Stage any offline ping/SNMP captures required for the connectivity lab so students can work without live gear.

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Welcome, expectations, and NetOps modernization briefing | Capture student goals and tie them to the exit ticket artifacts. |
| 09:25-10:20 | Block 2 (55 min) | Python refresher aligned to network data structures | Live-code parsing device metadata and show how fixtures map to lab scripts. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage students to explore `assets/gns3/topology-diagram.png`. |
| 10:30-11:25 | Block 3 (55 min) | Lab 01 walkthrough: building an inventory from static data | Pair students and demonstrate validating against offline CSV fixtures. |
| 11:25-12:20 | Block 4 (55 min) | Lab 02 setup: connectivity probes and reachability baselines | Emphasize diffing outputs before contacting real devices. |
| 12:20-13:05 | Lunch (45 min) | Recharge | Queue optional reading on NetOps community resources. |
| 13:05-14:00 | Block 5 (55 min) | Python modules for transport (paramiko/netmiko primers) | Highlight failure modes and logging patterns. |
| 14:00-14:10 | Break (10 min) | Reset | Offer optional mini-review for students new to Python. |
| 14:10-15:05 | Block 6 (55 min) | Guided lab time: students codify reachability checks | Coach teams to use the offline fixture before hitting GNS3 routers. |
| 15:05-16:00 | Block 7 (55 min) | Debrief and storytelling: converting raw checks into reports | Collect sample outputs for tomorrow's warm start. |
| 16:00-16:55 | Block 8 (55 min) | Capstone prep: translating checks into exit ticket summary | Show preview of Day 2 expectations and assign reflection prompts. |

## Exit Ticket
- Each team submits a reachability summary with the offline baseline diff and notes on which probes will extend to production gear tomorrow.
DOC

cat <<'DOC' > day01_foundations_connectivity/STUDENT.md
# Day 1 Student Guide — Foundations & Connectivity

## What you'll produce today
- A Python-driven device inventory exported to CSV and Markdown.
- Connectivity baselines validated against offline fixtures and GNS3 devices.
- A short reflection summarizing readiness for SNMP/syslog instrumentation.

## Steps
1. Review the lab topology in `assets/gns3/topology-diagram.png` and confirm device credentials in `assets/gns3/login-table.md`.
2. Activate the course virtual environment with `source .venv/bin/activate` (run `bash environment/bootstrap.sh` first if needed).
3. Complete Lab 01 (`day01_foundations_connectivity/labs/01_inventory/README.md`) using the provided starter fixture before touching live gear.
4. Use the offline ping results in `day01_foundations_connectivity/labs/02_connectivity/starter` to script reachability checks, then repeat against the GNS3 environment.
5. Capture screenshots or terminal output as evidence for your exit ticket recap.
6. Document open questions for tomorrow's SNMP/syslog instrumentation in your team notes.
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/01_inventory/README.md
# Lab 01 — Inventory

Transform offline device metadata into a shareable inventory using Python dictionaries and structured output.

## Resources
- Starter fixtures and scaffolding: `starter/`
- Expected outputs for validation: `expected_output/`

## Notes
- Begin with the offline dataset before connecting to GNS3 nodes.
- Highlight how students can extend the inventory to include SNMP capabilities on Day 2.
- [TODO: Update fixture filenames and targets for the current customer environment.]
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/01_inventory/starter/README.md
# Starter Materials

- Static device metadata sample for inventory generation.
- Skeleton Python script with TODO markers for students to fill in.
- [TODO: Confirm device list and add anonymized customer-relevant fields.]
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/01_inventory/expected_output/README.md
# Expected Output

- CSV inventory with hostname, role, IP, and platform columns.
- Markdown summary for executive stakeholders.
- [TODO: Attach sanitized sample outputs aligned to your environment.]
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/02_connectivity/README.md
# Lab 02 — Connectivity Baselines

Automate reachability checks using ping, TCP socket tests, and optional traceroutes while comparing against offline fixtures.

## Resources
- Starter scripts and baseline captures: `starter/`
- Expected outputs for reference: `expected_output/`

## Notes
- Encourage students to compare offline fixture results to live GNS3 tests before escalating failures.
- Reinforce logging patterns that will feed Day 2 syslog enrichment.
- [TODO: Embed sanitized ping/traceroute samples for this cohort.]
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/02_connectivity/starter/README.md
# Starter Materials

- Sample ping outputs for each device role.
- Stubs for reachability test functions with docstrings.
- [TODO: Add sanitized traceroute captures relevant to the client topology.]
DOC

cat <<'DOC' > day01_foundations_connectivity/labs/02_connectivity/expected_output/README.md
# Expected Output

- JSON report summarizing reachability state per device.
- Markdown briefing summarizing successes, failures, and remediation plan.
- [TODO: Provide anonymized example reports aligned to production conventions.]
DOC

cat <<'DOC' > day02_snmp_syslog/INSTRUCTOR.md
# Day 2 Instructor Guide — SNMP & Syslog Automation

## Objectives
- Extend inventory data with SNMP-derived attributes and syslog enrichment.
- Teach students to parse semi-structured telemetry into actionable events.
- Prepare teams to feed Day 3 REST workflows with normalized device state.

## Prep
- Verify SNMP community strings or credentials in `assets/gns3/login-table.md`. [TODO: Confirm SNMP credentials.]
- Review offline SNMP walks and syslog captures in `day02_snmp_syslog/labs/03_parse_snmp_syslog/starter`.
- Ensure the syslog parsing scripts run cleanly inside the virtual environment.

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Recap Day 1 outputs and map them to telemetry needs | Showcase how today's telemetry augments yesterday's inventory. |
| 09:25-10:20 | Block 2 (55 min) | SNMP fundamentals refresher with practical polling examples | Highlight pitfalls around versions, auth, and privacy settings. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage hydration and quick hallway questions. |
| 10:30-11:25 | Block 3 (55 min) | Lab 03 setup: parsing offline SNMP walks | Guide students through MIB lookups and fixture validation. |
| 11:25-12:20 | Block 4 (55 min) | Syslog parsing pipeline and message normalization | Demonstrate regex vs. TextFSM trade-offs. |
| 12:20-13:05 | Lunch (45 min) | Recharge | Seed conversation topics around telemetry aggregation. |
| 13:05-14:00 | Block 5 (55 min) | Guided lab time: build telemetry enrichment scripts | Coach teams on structuring output for REST ingestion. |
| 14:00-14:10 | Break (10 min) | Reset | Offer office-hours style debugging for straggling students. |
| 14:10-15:05 | Block 6 (55 min) | Integrate SNMP/syslog outputs with Day 1 inventory | Emphasize data cleanliness and schema evolution. |
| 15:05-16:00 | Block 7 (55 min) | Telemetry storytelling and alert design | Share customer wins and highlight Day 3 REST tie-ins. |
| 16:00-16:55 | Block 8 (55 min) | Exit ticket prep and optional stretch exercises | Assign stretch: convert a syslog event into a REST alert payload. |

## Exit Ticket
- Students submit a merged dataset showing SNMP attributes and parsed syslog events linked to the inventory entries.
DOC

cat <<'DOC' > day02_snmp_syslog/STUDENT.md
# Day 2 Student Guide — SNMP & Syslog Automation

## What you'll produce today
- SNMP-enriched device inventory with uptime, interface counts, and key OIDs.
- Parsed syslog events categorized by severity and mapped to your inventory.
- A draft alerting story that feeds tomorrow's REST API exercises.

## Steps
1. Revisit `assets/gns3/login-table.md` for SNMP credentials and confirm the topology in `assets/gns3/topology-diagram.png`.
2. Activate the course virtual environment (`source .venv/bin/activate`).
3. Work through Lab 03 (`day02_snmp_syslog/labs/03_parse_snmp_syslog/README.md`) using the offline SNMP walks before polling live devices.
4. Parse the syslog fixture to categorize events, then replay the workflow against your GNS3 syslog stream.
5. Merge telemetry outputs with yesterday's inventory and capture highlights for the exit ticket.
6. Draft REST payload fields you expect to need tomorrow and note any gaps.

DOC

cat <<'DOC' > day02_snmp_syslog/labs/03_parse_snmp_syslog/README.md
# Lab 03 — Parse SNMP & Syslog

Convert raw SNMP walk data and syslog messages into normalized structures that augment the device inventory.

## Resources
- Offline SNMP walks and syslog samples: `starter/`
- Reference outputs and validation helpers: `expected_output/`

## Notes
- Emphasize working offline first to avoid noisy lab environments.
- Encourage students to build parsers that tolerate vendor-specific quirks.
- [TODO: Update fixture filenames and OIDs to match the customer estate.]
DOC

cat <<'DOC' > day02_snmp_syslog/labs/03_parse_snmp_syslog/starter/README.md
# Starter Materials

- SNMP walk text files for each device role.
- Sample syslog archives with mixed severities.
- Parsing scaffolds demonstrating TextFSM and regex approaches.
- [TODO: Drop in sanitized production-like telemetry samples.]
DOC

cat <<'DOC' > day02_snmp_syslog/labs/03_parse_snmp_syslog/expected_output/README.md
# Expected Output

- Structured JSON records combining inventory data with SNMP attributes.
- Syslog event catalog grouped by severity and device role.
- [TODO: Provide anonymized sample outputs and instructor answer keys.]
DOC

cat <<'DOC' > day03_rest_apis/INSTRUCTOR.md
# Day 3 Instructor Guide — REST APIs & Orchestration

## Objectives
- Bridge telemetry insights into RESTful workflows and ticketing integrations.
- Teach students to consume vendor APIs and build lightweight orchestration.
- Prepare teams for Day 4 configuration automation requirements.

## Prep
- Validate REST API credentials or tokens for the target platforms. [TODO: Insert API endpoint details.]
- Review the offline API fixtures in `day03_rest_apis/labs/04_rest_apis/starter`.
- Ensure Postman or curl-based demos are ready for classroom projection.

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Recap telemetry outputs and map to REST use cases | Illustrate how REST APIs close the loop between insight and action. |
| 09:25-10:20 | Block 2 (55 min) | REST fundamentals, authentication patterns, and tooling | Demo curl + Python `requests` against a mock endpoint. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage students to rotate pairing partners. |
| 10:30-11:25 | Block 3 (55 min) | Lab 04 walkthrough: consuming offline API fixtures | Highlight schema validation and error handling. |
| 11:25-12:20 | Block 4 (55 min) | Mapping telemetry to REST payloads | Show how parsed syslog events become ticket updates. |
| 12:20-13:05 | Lunch (45 min) | Recharge | Suggest optional reading on vendor API rate limits. |
| 13:05-14:00 | Block 5 (55 min) | Guided lab time: build automation around REST calls | Reinforce idempotency and retry strategies. |
| 14:00-14:10 | Break (10 min) | Reset | Offer quick Q&A on authentication troubleshooting. |
| 14:10-15:05 | Block 6 (55 min) | Integrate API outputs with Day 2 telemetry | Show students how to persist results for Ansible consumption. |
| 15:05-16:00 | Block 7 (55 min) | Case studies: multi-vendor REST orchestration | Present success stories and pitfalls. |
| 16:00-16:55 | Block 8 (55 min) | Exit ticket prep and Day 4 preview | Connect API data to upcoming configuration automation goals. |

## Exit Ticket
- Teams submit a REST-driven workflow that ingests telemetry and produces a change recommendation or ticket update.
DOC

cat <<'DOC' > day03_rest_apis/STUDENT.md
# Day 3 Student Guide — REST APIs & Orchestration

## What you'll produce today
- A Python script that authenticates to a REST endpoint and retrieves actionable data.
- A workflow that converts SNMP/syslog insights into RESTful change or ticket updates.
- Notes capturing API limitations and prerequisites for tomorrow's configuration push.

## Steps
1. Review API targets and sample payloads in `day03_rest_apis/labs/04_rest_apis/starter`.
2. Ensure the course virtual environment is active (`source .venv/bin/activate`).
3. Complete Lab 04 (`day03_rest_apis/labs/04_rest_apis/README.md`) using the offline fixtures before hitting real APIs.
4. Map telemetry fields from Day 2 into REST payloads and document assumptions.
5. Capture request/response examples for your exit ticket.
6. Identify which responses should feed into Day 4 configuration automation and note required transforms.

DOC

cat <<'DOC' > day03_rest_apis/labs/04_rest_apis/README.md
# Lab 04 — REST APIs

Practice authenticating, sending, and parsing REST calls using the `requests` library and offline fixtures.

## Resources
- Mock API responses, Postman collections, and scaffolding: `starter/`
- Validation aids and annotated outputs: `expected_output/`

## Notes
- Emphasize error handling—time-outs, 4xx, and 5xx responses.
- Encourage students to log payloads for reuse in Day 4 Ansible playbooks.
- [TODO: Update mock payloads to reflect current customer services or NMS platforms.]
DOC

cat <<'DOC' > day03_rest_apis/labs/04_rest_apis/starter/README.md
# Starter Materials

- Postman collection and environment variables for the mock API.
- Python scaffolding with helper functions for authentication and pagination.
- [TODO: Add sanitized API tokens or instructions for obtaining sandbox credentials.]
DOC

cat <<'DOC' > day03_rest_apis/labs/04_rest_apis/expected_output/README.md
# Expected Output

- JSON responses annotated with key fields students must process.
- Markdown summary translating REST responses into action items.
- [TODO: Provide instructor reference solutions and troubleshooting tips.]
DOC

cat <<'DOC' > day04_config_and_ansible/INSTRUCTOR.md
# Day 4 Instructor Guide — Configuration & Ansible

## Objectives
- Translate REST and telemetry insights into configuration changes.
- Introduce Ansible for network automation while reinforcing idempotent practices.
- Prepare teams to integrate all artifacts into the final capstone.

## Prep
- Verify device credentials and Ansible inventory entries in `assets/gns3/login-table.md`.
- Review `day04_config_and_ansible/labs/05_config_vlan/starter` and `day04_config_and_ansible/labs/06_ansible_intro/starter`.
- Pre-test Ansible connectivity inside the course virtual environment.

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Recap REST outcomes and identify configuration gaps | Highlight change-control best practices. |
| 09:25-10:20 | Block 2 (55 min) | Python-based configuration push patterns | Show how to safely render templates with Jinja2. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage students to stretch. |
| 10:30-11:25 | Block 3 (55 min) | Lab 05 setup: VLAN configuration from REST insights | Walk through diffing generated configs against offline fixtures. |
| 11:25-12:20 | Block 4 (55 min) | Introduction to Ansible for NetOps | Demo inventory, playbooks, and idempotent checks. |
| 12:20-13:05 | Lunch (45 min) | Recharge | Share recommended Ansible community roles. |
| 13:05-14:00 | Block 5 (55 min) | Lab 06 guided build: first Ansible playbook | Emphasize dry runs and check mode. |
| 14:00-14:10 | Break (10 min) | Reset | Offer troubleshooting clinic for Ansible auth errors. |
| 14:10-15:05 | Block 6 (55 min) | Student lab time: integrate Python renders with Ansible | Coach on variable management and secrets handling. |
| 15:05-16:00 | Block 7 (55 min) | Multi-vendor considerations and rollback strategies | Showcase stories where Ansible saved time in change windows. |
| 16:00-16:55 | Block 8 (55 min) | Capstone planning and exit ticket prep | Align deliverables for tomorrow's presentation. |

## Exit Ticket
- Students submit rendered configs, Ansible playbooks, and a validation plan referencing REST and telemetry data.
DOC

cat <<'DOC' > day04_config_and_ansible/STUDENT.md
# Day 4 Student Guide — Configuration & Ansible

## What you'll produce today
- Rendered configuration snippets driven by REST and telemetry insights.
- An Ansible inventory and playbook capable of deploying the changes in check mode and apply mode.
- A validation checklist to prove the change succeeded.

## Steps
1. Review upcoming changes in `day04_config_and_ansible/labs/05_config_vlan/README.md` and confirm target devices in `assets/gns3/login-table.md`.
2. Activate the course virtual environment (`source .venv/bin/activate`).
3. Complete Lab 05 using the offline fixtures to render configurations before touching GNS3.
4. Move to Lab 06 to build an Ansible playbook; test in `--check` mode against GNS3.
5. Document diffs and validation evidence for your exit ticket.
6. Note any gaps you must close during tomorrow's capstone rehearsal.

DOC

cat <<'DOC' > day04_config_and_ansible/labs/05_config_vlan/README.md
# Lab 05 — Configuration VLAN

Render and validate VLAN configuration snippets based on insights gathered from REST APIs and telemetry.

## Resources
- Jinja2 templates and fixture data: `starter/`
- Reference outputs and validation scripts: `expected_output/`

## Notes
- Stress offline rendering and diffing prior to any live configuration push.
- Encourage consistent variable naming so Ansible can reuse the data.
- [TODO: Update template placeholders to match the customer's VLAN schema.]
DOC

cat <<'DOC' > day04_config_and_ansible/labs/05_config_vlan/starter/README.md
# Starter Materials

- Jinja2 templates for VLAN definitions.
- YAML fixture mapping telemetry insights to configuration intent.
- [TODO: Populate sample interfaces and segmentation requirements.]
DOC

cat <<'DOC' > day04_config_and_ansible/labs/05_config_vlan/expected_output/README.md
# Expected Output

- Validated configuration snippets ready for deployment.
- Diff reports demonstrating idempotent changes.
- [TODO: Provide anonymized diffs and validation transcripts.]
DOC

cat <<'DOC' > day04_config_and_ansible/labs/06_ansible_intro/README.md
# Lab 06 — Ansible Intro

Build an Ansible inventory and playbook that applies the rendered configurations with confidence.

## Resources
- Inventory and playbook skeletons: `starter/`
- Instructor-validated outputs and logs: `expected_output/`

## Notes
- Keep secrets out of source control and demonstrate vault usage if time allows.
- Require students to run in check mode before applying changes.
- [TODO: Add customer-specific variables and credential handling guidance.]
DOC

cat <<'DOC' > day04_config_and_ansible/labs/06_ansible_intro/starter/README.md
# Starter Materials

- Ansible inventory sample with group_vars structure.
- Playbook skeleton covering config deployment and validation tasks.
- [TODO: Insert sanitized credentials guidance and per-device notes.]
DOC

cat <<'DOC' > day04_config_and_ansible/labs/06_ansible_intro/expected_output/README.md
# Expected Output

- Successful `ansible-playbook` run in check and apply modes.
- Post-change validation evidence linked to telemetry dashboards.
- [TODO: Provide sample playbook output and validation logs.]
DOC

cat <<'DOC' > day05_capstone/INSTRUCTOR.md
# Day 5 Instructor Guide — Capstone Integration

## Objectives
- Guide teams through a full-stack automation narrative tying together inventory, telemetry, REST, and configuration.
- Coach students on storytelling and stakeholder-ready presentations.
- Validate technical and communication readiness for production rollout.

## Prep
- Curate exemplary artifacts from Days 1–4 for reference.
- Confirm presentation logistics (room setup, projector, timing).
- Prepare rubric for technical depth, collaboration, and presentation clarity. [TODO: Attach rubric.]

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Capstone kickoff and expectations | Outline deliverables and success criteria. |
| 09:25-10:20 | Block 2 (55 min) | Team work session: finalize automation flow | Circulate to unblock technical issues. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage teams to rehearse talking points. |
| 10:30-11:25 | Block 3 (55 min) | Technical deep dives | Provide targeted coaching on weak areas. |
| 11:25-12:20 | Block 4 (55 min) | Presentation dry runs | Give time-boxed feedback per team. |
| 12:20-13:05 | Lunch (45 min) | Recharge | Remind teams of presentation order. |
| 13:05-14:00 | Block 5 (55 min) | Final preparation and artifact polishing | Ensure supporting files are in repo folders. |
| 14:00-14:10 | Break (10 min) | Reset | Set expectations for Q&A during presentations. |
| 14:10-15:05 | Block 6 (55 min) | Capstone presentations (teams 1–2) | Timebox to allow Q&A. |
| 15:05-16:00 | Block 7 (55 min) | Capstone presentations (teams 3–4) | Capture action items and feedback. |
| 16:00-16:55 | Block 8 (55 min) | Course retrospective and next steps | Align on post-course adoption plan. |

## Exit Ticket
- Teams deliver a documented automation playbook plus a presentation demonstrating how each component ties to customer outcomes.
DOC

cat <<'DOC' > day05_capstone/STUDENT.md
# Day 5 Student Guide — Capstone Integration

## What you'll produce today
- A cohesive automation storyline that links inventory, telemetry, REST workflows, and configuration changes.
- A polished presentation with evidence, code pointers, and next-step recommendations.
- A retrospective documenting team lessons learned and production readiness items.

## Steps
1. Consolidate artifacts from Days 1–4 inside your team folder; ensure screenshots in `assets/gns3/` are up to date.
2. Activate the virtual environment (`source .venv/bin/activate`) to run any final scripts.
3. Build the end-to-end demo flow, validating each stage with offline fixtures before live execution.
4. Rehearse your presentation, ensuring everyone speaks to a portion of the automation story.
5. Capture outstanding risks or follow-ups to highlight during the retrospective.
6. Submit your final artifacts and slide deck to the instructor before presentations begin.
DOC

cat <<'DOC' > environment/requirements.txt
requests==2.31.0
PyYAML==6.0.1
Jinja2==3.1.3
netmiko==4.3.0
napalm==4.1.0
textfsm==1.1.3
pysnmp==4.4.12
ansible-core==2.15.9
DOC

cat <<'DOC' > environment/bootstrap.sh
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

pip install --upgrade pip
pip install -r "${ROOT_DIR}/environment/requirements.txt"

python <<'PY'
import importlib

modules = [
    "requests",
    "yaml",
    "jinja2",
    "netmiko",
    "napalm",
    "textfsm",
    "pysnmp",
    "ansible"
]

for module in modules:
    importlib.import_module(module)

print("Smoke test imports succeeded.")
PY


echo "Virtual environment ready. Activate with: source \"${VENV_DIR}/bin/activate\""
DOC

chmod +x environment/bootstrap.sh
chmod +x history_scrub.sh verify_scrub.sh
