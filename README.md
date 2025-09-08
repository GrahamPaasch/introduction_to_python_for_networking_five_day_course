# Python 3.11 for Network Engineers — 5‑Day Intensive (Cisco & Juniper)

This repository contains the full curriculum, labs, and setup for a 5‑day, production‑safe, hands‑on training focused on Python 3.11 network automation for Cisco IOS XE / NX‑OS and Juniper Junos (including applicable firewall workflows).

Audience: 5–15 years network engineering experience; Python beginner. Delivery: remote across US/EU time zones. Devices: 2 per student (sandbox/sim).

Vendor targets and tooling: Netmiko 4.x, NAPALM 3.x, Nornir 3.x, Ansible (core + collections), Requests ≥2.32, HTTPX (sync), Jinja2 (templates), pysnmp (SNMP), Python stdlib json, concurrent.futures. Vendor APIs: Cisco RESTCONF, Junos REST API. Lab backends: Cisco DevNet Sandbox, Juniper vLabs; fallbacks: httpbin.org and jsonplaceholder.typicode.com. No production changes.


## Section A: One‑page overview

Goals
- Build reliable, idempotent Python 3.11 automation for Cisco IOS XE / NX‑OS and Juniper Junos.
- Confidently use device CLI (Netmiko), NAPALM getters, RESTCONF (Cisco), and Junos REST.
- Model inventory data (YAML/CSV → JSON/SQLite) and execute safe parallel fan‑out with timeouts/retries.
- Deliver a capstone: multi‑vendor VLAN + interface config + inventory + API query, demoed live.

Outcomes → Assessments mapping
- Python & stdlib proficiency (syntax, data types, flow, functions, modules, error handling, logging, JSON) → Daily checks + code review checklist.
- Device access & parsing (Netmiko + TextFSM or NAPALM) → Day 1/2 labs artifacts validated by parsers and unit checks.
- REST APIs (Requests/HTTPX) with auth and error handling → Day 3 labs with GET/POST/PUT/DELETE success criteria.
- Idempotent multi‑vendor config → Day 4 lab showing no‑op on repeat run and clean diffs.
- Concurrency fan‑out with backoff/timeouts → Day 4 lab timed run and retry logs.
- Ansible intro (bonus) → Day 4/5 optional playbook validation (check mode) and dry‑run logs.
- Capstone integration → Day 5 demo; post‑quiz verifies conceptual understanding.

Prerequisites
- Python 3.11 installed on Windows 11, macOS, or Ubuntu; ability to create a venv and use pip.
- Git installed; one private repo per student (policy provided below).
- Access to Cisco DevNet Sandbox and Juniper vLabs accounts, or ability to use mocks via httpbin/jsonplaceholder.
- No production access; secrets via environment variables or Ansible Vault.

Repo structure
```
common/
	lib/            # shared Python helpers (logging, session, utils)
	inventory/      # YAML/CSV inputs and derived JSON/SQLite
		templates/      # Jinja2 templates for config text
day1_setup/
day2_cli_to_data/
day3_rest_and_json/
day4_multivendor_config/
day5_capstone/
```


## Section B: Daily timetable and deliverables

Schedule: 07:00–16:30 with a single 30‑minute lunch (12:00–12:30). Two short breaks morning and afternoon. All times local to each cohort; recordings provided for other time zones.

Day 1 — Python Foundations + Safe Device Access (≤40% lecture, ≥60% lab)
- 07:00–07:20 — Kickoff, goals, safety, sandboxes
- 07:20–08:00 — Lecture: Python 3.11 basics (syntax, data types, flow)
- 08:00–09:30 — Lab 1.1: Workstation setup + venv + package checks
- 09:30–09:40 — Break
- 09:40–10:20 — Lecture: functions, modules, error handling, logging
- 10:20–12:00 — Lab 1.2: Inventory from CSV/YAML → JSON; basic CLI parsing (see `day1_setup/06_inventory_bootstrap.py`)
- 12:00–12:30 — Lunch
- 12:30–13:00 — Lecture: TextFSM vs NAPALM getters; JSON handling
- 13:00–15:00 — Lab 1.3: Netmiko show commands (routers/switches/firewalls); parse and persist
- 15:00–15:10 — Break
- 15:10–16:00 — Checkpoint + daily quiz
- 16:00–16:30 — Office hours / timezone Q&A

Expected artifacts
- Verified venv with pinned libs, `inventory.json`, parsed `show` outputs in JSON.

Day 2 — From CLI to Structured Data (NAPALM) and Persistence
- 07:00–07:20 — Recap and Q&A
- 07:20–08:00 — Lecture: NAPALM, data modeling, SQLite basics
- 08:00–09:40 — Lab 2.1: NAPALM getters (facts, interfaces, routes)
- 09:40–09:50 — Break
- 09:50–11:30 — Lab 2.2: YAML/CSV → JSON/SQLite inventory persistence
- 11:30–12:00 — Mini‑talk: logging patterns and error taxonomies
- 12:00–12:30 — Lunch
- 12:30–13:00 — Lecture: Unit checks and validation scripts
- 13:00–15:10 — Lab 2.3: Validation scripts + simple reports
- 15:10–15:20 — Break
- 15:20–16:10 — Checkpoint + code reviews
- 16:10–16:30 — Office hours

Expected artifacts
- `inventory.db` SQLite with facts tables; validation scripts with exit codes.

Day 3 — REST, JSON, and Vendor APIs
- 07:00–07:20 — Lecture: HTTP, JSON, auth, status codes, retries
- 07:20–09:30 — Lab 3.1: Cisco RESTCONF GET/PUT; httpbin mocks if needed
- 09:30–09:40 — Break
- 09:40–11:10 — Lab 3.2: Junos REST GET/POST/DELETE (validate‑only)
- 11:10–12:00 — Lecture: API error handling, rate limiting, pagination
- 12:00–12:30 — Lunch
- 12:30–13:00 — Lecture: Concurrency basics (ThreadPoolExecutor)
- 13:00–15:00 — Lab 3.3: HTTP fan‑out with timeouts/retries/backoff
- 15:00–15:10 — Break
- 15:10–16:10 — Checkpoint + daily quiz
- 16:10–16:30 — Office hours

Expected artifacts
- RESTCONF and Junos REST scripts with idempotent operations; fan‑out utility.
- Offline fixtures for restricted environments; set `OFFLINE=1` to use.
- Optional labs: XML parsing + strings, SNMP minimal, config diff demo.

Day 4 — Idempotent Multi‑Vendor Configuration + Parallelism
- 07:00–07:20 — Lecture: Idempotence patterns; dry‑run; diffs
- 07:20–09:40 — Lab 4.1: Threaded CLI/NAPALM gather with retries
- 09:40–09:50 — Break
- 09:50–12:00 — Lab 4.2: VLAN + interface description (Cisco IOS XE/NX‑OS/Junos)
- 12:00–12:30 — Lunch
- 12:30–13:00 — Lecture: Intro to Ansible for network automation
- 13:00–15:00 — Lab 4.3 (bonus): Ansible inventory + playbooks (check mode)
- 15:00–15:10 — Break
- 15:10–16:10 — Code review + capstone scaffolding
- 16:10–16:30 — Office hours

Expected artifacts
- Re‑runnable config scripts with no‑op second run; diffs captured in logs; Ansible playbooks (optional).
- Orchestrator: `day4_multivendor_config/configure_multivendor.py` (VLAN + interface desc).

Day 5 — Capstone Build and Demo
- 07:00–07:20 — Lecture: Putting it together; demo tips
- 07:20–10:30 — Lab 5.1: Capstone integration and tests
- 10:30–10:40 — Break
- 10:40–12:00 — Lab 5.2: Capstone dry‑run then sandbox apply
- 12:00–12:30 — Lunch
- 12:30–14:30 — Capstone demos (5–7 min/team)
- 14:30–15:00 — Post‑quiz
- 15:00–16:00 — Retrospective and next steps
- 16:00–16:30 — Office hours

Expected artifacts
- Working capstone that configures VLAN and interface descriptions idempotently and performs an API query across inventory with parallelism.

## Validation & Offline Modes

- Concept: “Validation” are quick, scriptable checks that prove a lab’s outcome. Prefer commands that return clear success/failure via exit codes and log snippets.
- Offline: When internet access is unavailable, set `OFFLINE=1` to switch certain labs to local fixtures under `common/fixtures/`.

Cheat sheet
- Day 1 basics: run `python day1_setup/01_python_basics.py` and confirm INFO logs.
- XML + strings: `python day1_setup/05_xml_and_strings.py` → outputs `common/outputs/devices_from_xml.json`.
- Inventory bootstrap: `python day1_setup/06_inventory_bootstrap.py` → writes `common/outputs/devices.json`.
- Syslog parsing: `python day2_cli_to_data/04_syslog_parse.py` → outputs `common/outputs/syslog_events.json` (non‑empty).
- Inventory persist: `python day2_cli_to_data/00_inventory_persist.py` → creates `common/outputs/devices.json` and `common/outputs/inventory.sqlite`.
- NAPALM getters: `OFFLINE=1 python day2_cli_to_data/02_napalm_getters.py` → writes `common/outputs/napalm_results.json`.
- SNMP minimal: `OFFLINE=1 python day2_cli_to_data/05_snmp_minimal.py` → writes `common/outputs/snmp_ifaces.json`.
- RESTCONF: `OFFLINE=1 python day3_rest_and_json/01_restconf_requests.py` → prints interfaces + mock objects without network.
- Junos REST: `OFFLINE=1 python day3_rest_and_json/02_junos_rest_httpx.py` → prints software info from fixtures.
- Parallel fan‑out: `python day4_multivendor_config/02_parallel_fanout.py` (requires reachable devices) — success logs per host.
- Multi‑vendor config: dry‑run `python day4_multivendor_config/configure_multivendor.py` then set `COMMIT=true` to apply; second run should show “no changes”.
- Config diff demo: `python day4_multivendor_config/04_config_diff_demo.py` prints unified diff from fixtures.

- Run multiple validations quickly: `python scripts/run_validations.py` (defaults to `OFFLINE=1`).

Notes
- All config scripts default to dry‑run. Set `COMMIT=true` to apply changes.
- Environment secrets via `NET_USERNAME` and `NET_PASSWORD`.
 - `NET_SECRET` can be set for devices requiring enable/privileged mode (e.g., ASA).

## Ansible (Bonus)

- Inventories and playbook are in `ansible/`.
- Prefer check mode and syntax checks first:
  - `ansible-playbook -i ansible/inventory.yaml ansible/site.yaml --syntax-check`
  - `ansible-playbook -i ansible/inventory.yaml ansible/site.yaml --check -v`
- Collections (if internet available):
  - `ansible-galaxy collection install -r ansible/requirements.yml` (includes `community.network`, `cisco.ios`, `junipernetworks.junos`)
- In restricted environments, demo with `--syntax-check` and discuss idempotence; keep Python labs as primary hands‑on.

## Optional Mini‑Labs (High Impact)

- SNMP minimal (offline‑first): `day2_cli_to_data/05_snmp_minimal.py` — produces `snmp_ifaces.json` with interface up/down counts.
- XML parsing + strings: `day1_setup/05_xml_and_strings.py` — shows `split()`, `startswith()`, normalization, writes a small JSON.
- Config diff (stdlib): `day4_multivendor_config/04_config_diff_demo.py` — demonstrates diffs and idempotence concepts.
- Routing (OSPF) stretch: simple OSPF parameter update across platforms with validation (skeleton; optional).

See also: `CHEATSHEET.md` and `scripts/run_validations.py`.



## Section C: Lab briefs (purpose, steps, validation, cleanup)

Conventions
- Use a Python venv per repo. Install packages with pip in the venv.
- Secrets via env vars: LAB_USERNAME, LAB_PASSWORD. Optionally Ansible Vault for playbooks.
- Sandboxes: Cisco DevNet Sandbox (IOS XE always‑on: `sandbox-iosxe-latest-1.cisco.com:22/443`), Juniper vLabs device of your assignment.
- Fallbacks: use httpbin.org and jsonplaceholder.typicode.com when vendor access is unavailable.
- Windows PowerShell vs Linux/macOS shells shown separately.

Lab 1.1 — Workstation setup + package checks
- Purpose: Ensure Python 3.11 toolchain, venv, and required packages (Netmiko 4.x, NAPALM 3.x, Nornir 3.x, Requests ≥2.32, HTTPX, TextFSM, ntc‑templates, Ansible core) are installed; verify proxies and sandbox reachability.
- Prereqs: Internet; Git; non‑admin is OK.
- Steps (Windows PowerShell)
	1) Verify Python 3.11 and pip
		 ```powershell
		 python --version
		 py -3.11 --version
		 py -3.11 -m pip --version
		 ```
	2) Create venv and activate
		 ```powershell
		 py -3.11 -m venv .venv
		 .\.venv\Scripts\Activate.ps1
		 ```
	3) Optional proxy env
		 ```powershell
		 $env:HTTPS_PROXY="http://proxy:8080"; $env:HTTP_PROXY=$env:HTTPS_PROXY
		 ```
	4) Install packages (pinned major)
		 ```powershell
		 python -m pip install --upgrade pip
			 pip install "netmiko>=4,<5" "napalm>=3,<4" "nornir>=3,<4" "nornir-netmiko>=1,<2" "nornir-napalm>=0.4,<0.5" \
				 "requests>=2.32,<3" "httpx>=0.27,<1" textfsm ntc-templates "ansible-core>=2.16,<2.18" \
				 pyyaml sqlite-utils Jinja2 pysnmp
		 ```
	5) Version check
		 ```powershell
		 python - <<'PY'
import sys, importlib
mods = ['netmiko','napalm','nornir','requests','httpx','yaml']
print(sys.version)
for m in mods:
		try:
				v = importlib.import_module(m).__version__
		except Exception as e:
				v = f"? ({e})"
		print(f"{m}=={v}")
PY
		 ```
- Steps (Linux/macOS)
	1) Verify Python 3.11 and pip
		 ```bash
		 python3 --version || true
		 python3.11 --version
		 python3.11 -m pip --version
		 ```
	2) Create venv and activate
		 ```bash
		 python3.11 -m venv .venv
		 source .venv/bin/activate
		 ```
	3) Optional proxy env
		 ```bash
		 export HTTPS_PROXY=http://proxy:8080
		 export HTTP_PROXY=$HTTPS_PROXY
		 ```
	4) Install packages
		 ```bash
		 python -m pip install --upgrade pip
			 pip install "netmiko>=4,<5" "napalm>=3,<4" "nornir>=3,<4" "nornir-netmiko>=1,<2" "nornir-napalm>=0.4,<0.5" \
				 "requests>=2.32,<3" "httpx>=0.27,<1" textfsm ntc-templates "ansible-core>=2.16,<2.18" \
				 pyyaml sqlite-utils Jinja2 pysnmp
		 ```
- Validation
	- `python -c "import netmiko,napalm,requests,httpx; print('ok')"` prints ok.
	- `pip list` shows versions in requested ranges.
- Cleanup
	- Keep the venv active for all remaining labs.

Lab 1.2 — Inventory from CSV/YAML → JSON
- Purpose: Build a simple inventory pipeline ingesting CSV/YAML, emitting JSON persisted to `common/inventory/devices.json`.
- Prereqs: Completed Lab 1.1.
- Steps
	# Python 3.11 for Network Engineers — 5‑Day Hands‑On (Cisco IOS XE/NX‑OS & Juniper Junos)
	- JSON validates with `python -m json.tool common/inventory/devices.json`.
	- At least 2 devices present.
- Cleanup
	- None.

Lab 1.3 — Netmiko show commands; parse and persist
- Purpose: Safely collect `show` output with Netmiko, parse with TextFSM/ntc‑templates, and persist to JSON.
- Checkpoints
	- Re‑run script; it should skip writing if identical (idempotent write check via hash or compare).
	- Errors are logged to `day1_setup/run.log`; no stack traces printed by default.
- Cleanup
- Prereqs: Lab 1.2; credentials in env vars.
- Steps
- Expected output
	- `inventory.db` contains populated tables; counts printed.
- Purpose: Normalize inventory into both JSON and SQLite for later joins.
- Steps
	- Build `day2_cli_to_data/inventory_persist.py` that reads CSV/YAML, writes JSON and upserts into SQLite `devices` table.
	- Validate with a small query printing devices per OS.
- Expected output
- Purpose: Use Requests/HTTPX to query and modify data via RESTCONF on IOS XE; support dry‑run via `X-HTTP-Method-Override: GET` and safe checks.
- Prereqs: RESTCONF enabled on sandbox (DevNet IOS XE always‑on has it); creds.
	- JSON files under `day3_rest_and_json/outputs/iosxe_*.json`; logs with request IDs and timing.

- Expected output
	- Saved JSON responses; logs show validate‑only mode active.
Lab 4.1 — Threaded CLI/NAPALM gather with retries
- Purpose: Combine Netmiko and NAPALM collectors in parallel with robust error handling and structured outputs.
- Purpose: Apply VLAN creation and interface description updates across IOS XE, NX‑OS, and Junos using idempotent checks.
- Steps
	- Create `day4_multivendor_config/configure_multivendor.py`:
		- For IOS XE/NX‑OS (Netmiko): pre‑check `show run | sec vlan` and `show interface description`; only send commands if missing/mismatched. Verify with post‑check.
	- First run performs changes; second run is a no‑op; diffs logged.

Lab 4.3 (bonus) — Ansible: interface description + VLAN
- Purpose: Introduce idempotent playbooks and inventories for Cisco/Juniper using check mode.
- Steps
	- Create `day4_multivendor_config/ansible/hosts.yml` and `site.yml`.
	- Install required collections and run in `--check` first, then against sandboxes.
- Expected output
	- Check mode shows `changed=0` on second run; logs captured.

Lab 5.1/5.2 — Capstone integration and demo
- Purpose: Build and present an end‑to‑end automation: inventory → gather → API query → idempotent config → parallelism → reports.
- Steps
	- Provide a `day5_capstone/runner.py` orchestrating modules from `common/lib` and prior labs with `--dry-run` default; `--apply` flag required for changes. Include per‑vendor strategies and consolidated report.
	- Add a simple README and usage examples; run dry‑run, then apply in sandbox.


Python 3.11 install
- macOS: `brew install python@3.11` (Homebrew). Verify with `python3.11 --version`.
- Ubuntu: `sudo apt-get update && sudo apt-get install -y python3.11 python3.11-venv python3.11-distutils`.
- Windows PowerShell
	```powershell
	py -3.11 -m venv .venv
	```
- Linux/macOS bash/zsh
	source .venv/bin/activate
	```
Install packages
- In the venv on any OS
	pip install "netmiko>=4,<5" "napalm>=3,<4" "nornir>=3,<4" "nornir-netmiko>=1,<2" "nornir-napalm>=0.4,<0.5" \
	```

	```powershell
	$env:LAB_USERNAME = "developer"
	$env:LAB_JUNOS_PASS = "lab123"
	```
	```bash
	export LAB_USERNAME=developer
	export LAB_JUNOS_PASS=lab123
	```
Proxy settings (if needed)
- Windows PowerShell
	$env:HTTPS_PROXY = "http://proxy:8080"; $env:HTTP_PROXY = $env:HTTPS_PROXY
	```
	export HTTPS_PROXY=http://proxy:8080
	export HTTP_PROXY=$HTTPS_PROXY

Git repo policy
Sandbox sign‑in
- Cisco DevNet Sandbox: Create account, then reserve or use always‑on IOS XE (`sandbox-iosxe-latest-1.cisco.com`). Ensure RESTCONF is enabled (it is on always‑on). Use `developer` / published password.
## Section E: Assessment rubric and capstone spec

- One practical check (e.g., “Show your `inventory.db` with devices table count”).

Code review checklist (applies to all labs)
- Uses venv and pinned dependencies.
- No hard‑coded secrets; env vars or Vault used.
- Logging at INFO level to file; WARNING/ERROR surfaced to console.
- Timeouts and retries for all network I/O.
- JSON outputs validated; schema stable.

Capstone acceptance criteria
- Safety: No production devices; retries/timeout; clear rollback or no‑op guarantee on repeat.
- Observability: Logs with timestamps, per‑host status, and summary counts.

Post‑quiz (Day 5)
- 12–15 questions on Python basics, HTTP semantics, vendor API basics, idempotence, and concurrency.

## Section F: Reference links (official docs only)

Core Python
- Python 3.11: https://docs.python.org/3.11/
- Logging HOWTO: https://docs.python.org/3.11/howto/logging.html
- concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
Networking libraries
- Netmiko: https://ktbyers.github.io/netmiko/

HTTP clients
- HTTPX: https://www.python-httpx.org/

Parsing
- TextFSM: https://github.com/google/textfsm
Vendor APIs
- Cisco IOS XE RESTCONF: https://developer.cisco.com/docs/ios-xe/#!restconf/what-is-restconf
- Cisco DevNet Sandboxes: https://devnetsandbox.cisco.com/
- Junos REST API Guide: https://www.juniper.net/documentation/us/en/software/junos-apis/index.html
- Juniper vLabs: https://jlabs.juniper.net/vlabs/

- httpbin: https://httpbin.org/
- JSONPlaceholder: https://jsonplaceholder.typicode.com/

---
- No admin rights: use portable Python or pre‑created venv; avoid system installs.
- Corporate proxy: set HTTP(S)_PROXY env vars before pip or API calls.
Notes
- All configuration tasks default to dry‑run where supported; explicit `--apply` required for changes.
- Labs target safest available always‑on sandboxes and validate-only modes on Junos.
