# Day 02 — SNMP & Syslog (Observability)

## Learning outcomes
- Understand SNMP basics (OIDs, GET/WALK) and syslog severities/patterns.
- Ingest and parse SNMP + syslog into a simple health report.
- Persist summarized metrics and events for later policy checks.

## Materials & setup
- Slides (optional) — keep to <20 per day; demo beats slides.
- Whiteboard/markers for design discussions.
- Student repo cloned; `environment/bootstrap.sh` run; venv active.
- Access to `lab.grahampaasch.com`; GNS3 topology handy (see `docs/gns3.md`).

## Labs used today
- `labs/03_parse_snmp_syslog` — offline fixtures to build `health_report.json`

> **Schedule:** 8 x ~55‑min hours with two 10‑min breaks and a 45‑min lunch. Adjust to your start time.

## Hour‑by‑hour plan

### Hour 1: Observability overview (SNMP + syslog)
- OIDs, walks, common device MIBs; syslog levels and facility.
- Show examples from your topology; align to client asks.

### Hour 2: Parsing patterns & data shapes
- From raw text to dicts; counters vs gauges; summarization.
- Short break (10 min) at end of hour.

### Hour 3: Lab 03 (part A) — parse fixtures
- Parse `fixtures/snmp_walk.json` and `syslog_samples.log`.
- Count link flaps; compute CPU/mem equivalents per vendor.

### Hour 4: Lab 03 (part B) — build health report
- Write `expected_output/health_report.json`.
- Stretch: store into SQLite for easy joins later.

### Hour 5: Debrief + extensions
- Discuss thresholds and alerting vs reporting; tailing live logs.

### Hour 6: Mini‑exercise — add one vendor‑specific OID
- Students add a metric and adapt the parser.

### Hour 7: Quality gate — schema & unit test sketch
- Design a tiny schema; show a toy unit test (no devices).

### Hour 8: Review + exit ticket
- Students submit `health_report.json` and explain one parser choice.
- Preview tomorrow: REST APIs (RESTCONF/Junos REST).

## Plan‑B (offline)
- Run entirely on fixtures if lab is congested; inject your own sample logs.

## Assessment / Exit ticket
- `health_report.json` present with per‑device metrics and flap counts.
