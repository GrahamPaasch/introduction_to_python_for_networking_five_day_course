# Day 1 Instructor Guide — Foundations & Connectivity

## Objectives
- Align the cohort on the modern NetOps roadmap and course expectations.
- Demonstrate gathering inventory data with Python before touching production devices.
- Validate reachability using offline fixtures so students can compare with lab equipment.

## Prep
- Review `./labs/01_inventory/starter` fixtures and update hostnames, IPs, and device roles. [TODO: Confirm device list for this cohort.]
- Refresh the GNS3 project and verify screenshots in `click_me_09_gns3_assets/gns3/` reflect the current topology.
- Run `bash click_me_10_environment_setup/bootstrap.sh` to rebuild the virtual environment and smoke-test imports.
- Stage any offline ping/SNMP captures required for the connectivity lab so students can work without live gear.

## Schedule
| Time | Block | Focus | Instructor Notes |
| --- | --- | --- | --- |
| 08:30-09:25 | Block 1 (55 min) | Welcome, expectations, and NetOps modernization briefing | Capture student goals and tie them to the exit ticket artifacts. |
| 09:25-10:20 | Block 2 (55 min) | Python refresher aligned to network data structures | Live-code parsing device metadata and show how fixtures map to lab scripts. |
| 10:20-10:30 | Break (10 min) | Reset | Encourage students to explore `click_me_09_gns3_assets/gns3/topology-diagram.png`. |
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
