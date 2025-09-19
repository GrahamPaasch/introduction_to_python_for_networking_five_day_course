---
marp: true
title: Day 1 — Lab 1.3 Netmiko Show & Persist
paginate: true
---

# Lab 1.3 — Netmiko Show & Persist

- Connect safely
- Run read‑only commands
- Parse and store outputs

---

## Objectives

- Use `ConnectHandler` with timeouts
- Execute vendor‑specific show commands
- Parse with TextFSM where available

---

## Steps

1) Export `NET_USERNAME` / `NET_PASSWORD`
2) Optional: `NET_SECRET` (enable) for ASA
3) Run `python day2_cli_to_data/01_netmiko_show.py`

---

## Commands (Examples)

- IOS XE: `show version`, `show ip interface brief`
- NX‑OS: `show version`, `show interface brief`
- Junos: `show interfaces terse | display json`
- ASA: `show interface ip brief`

---

## Persist Results

- Capture stdout to file (shell redirect)
- Or adapt script to write JSON

---

## Idempotence Check

- Re‑run; output should be consistent
- Logs show timing and success per device

---

## Troubleshooting

- Timeouts → verify host/port/reachability
- Auth → env vars
- TextFSM template missing → raw text is OK

