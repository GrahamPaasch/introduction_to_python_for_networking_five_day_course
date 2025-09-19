# Day 4 Instructor Guide — Configuration & Ansible

## Objectives
- Translate REST and telemetry insights into configuration changes.
- Introduce Ansible for network automation while reinforcing idempotent practices.
- Prepare teams to integrate all artifacts into the final capstone.

## Prep
- Verify device credentials and Ansible inventory entries in `click_me_09_gns3_assets/gns3/login-table.md`.
- Review `./labs/05_config_vlan/starter` and `./labs/06_ansible_intro/starter`.
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
