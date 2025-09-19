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
