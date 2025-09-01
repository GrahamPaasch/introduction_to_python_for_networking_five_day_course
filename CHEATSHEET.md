# Python for Network Engineers — 1‑Page Cheat Sheet

- Env vars
  - `OFFLINE=1`: force fixture mode for REST/NAPALM/SNMP labs
  - `NET_USERNAME` / `NET_PASSWORD`: device creds override
  - `COMMIT=true`: apply changes (default is dry‑run)

- Quick runs
  - Day 1 basics: `python day1_setup/01_python_basics.py`
  - XML + strings: `python day1_setup/05_xml_and_strings.py`
  - CSV→YAML: `python day2_cli_to_data/03_csv_to_yaml.py common/inventory/devices.example.csv common/inventory/devices.example.yaml`
  - Inventory persist: `python day2_cli_to_data/00_inventory_persist.py`
  - Syslog parse: `python day2_cli_to_data/04_syslog_parse.py`
  - SNMP (offline): `OFFLINE=1 python day2_cli_to_data/05_snmp_minimal.py`
  - NAPALM getters (offline): `OFFLINE=1 python day2_cli_to_data/02_napalm_getters.py`
  - RESTCONF (offline): `OFFLINE=1 python day3_rest_and_json/01_restconf_requests.py`
  - Junos REST (offline): `OFFLINE=1 python day3_rest_and_json/02_junos_rest_httpx.py`
  - Fan‑out: `python day4_multivendor_config/02_parallel_fanout.py`
  - Multivendor config dry‑run: `python day4_multivendor_config/configure_multivendor.py`
  - Apply changes: `COMMIT=true python day4_multivendor_config/configure_multivendor.py`

- Validation runner
  - `python scripts/run_validations.py` (defaults to OFFLINE)

- Patterns
  - Idempotence: design scripts so second run is a no‑op
  - Logging: INFO → file + console; WARNING/ERROR for failures
  - Timeouts + retries for all network I/O
  - Secrets via env vars, never in code

- Helpful stdlib
  - `json`, `csv`, `sqlite3`, `ipaddress`, `difflib`, `argparse`, `pathlib`

