---
title: Slides — Python 3.11 for Network Engineers (5‑Day)
marp: true
paginate: true
---

# Slides Overview

- Format: Markdown decks compatible with Marp (VS Code Marp extension or marp-cli)
- Export: Open a `.md` deck in VS Code → Marp: Export slide deck (PDF/PPTX)
- Structure: `slides/dayN/NN_topic.md` per subject per day

## Rendering Locally

- VS Code: Install “Marp for VS Code” extension; open a deck and export
- CLI (optional): `npm i -g @marp-team/marp-cli` then `marp slides/day1/01_orientation_use_cases.md`

## Deck Index

- Day 1: Orientation & Python basics, inventory bootstrap, TextFSM vs NAPALM, Netmiko show lab
- Day 2: Data structures, SQLite, NAPALM getters, inventory persistence lab, syslog parsing, validation scripts
- Day 3: HTTP/JSON/auth, RESTCONF (IOS XE), Junos REST, error handling & pagination, concurrency, fan‑out lab
- Day 4: Idempotence, templates & diffs, threaded gather, multi‑vendor VLAN+iface, Ansible intro, config diff demo
- Day 5: Design review & guardrails, capstone orchestration, presentations & post‑quiz, next steps

## Exports

- CI builds PDF and PPTX into `slides/exports/` on every push affecting `slides/**/*.md`.
- You can also run Marp locally if preferred (see above).
