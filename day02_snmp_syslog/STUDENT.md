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

