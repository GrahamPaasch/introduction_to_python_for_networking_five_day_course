# Day 2 Instructor Guide — SNMP & Syslog Automation

## Objectives
- Extend inventory data with SNMP-derived attributes and syslog enrichment.
- Teach students to parse semi-structured telemetry into actionable events.
- Prepare teams to feed Day 3 REST workflows with normalized device state.

## Prep
- Verify SNMP community strings or credentials in `click_me_09_gns3_assets/gns3/login-table.md`. [TODO: Confirm SNMP credentials.]
- Review offline SNMP walks and syslog captures in `./labs/03_parse_snmp_syslog/starter`.
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
