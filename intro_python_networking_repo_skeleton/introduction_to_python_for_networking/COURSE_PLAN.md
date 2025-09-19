# 5‑day teaching plan (8h/day)

**Day 1 — Foundations & Device Access**  
- Modern NetOps use‑cases; Python vs Ansible roles.  
- Python essentials (functions, exceptions, logging).  
- Netmiko safe connectivity; prompt/privilege handling.  
- **Lab 01:** Inventory bootstrap → connect → gather facts → SQLite/JSON.

**Day 2 — Data, SNMP & Syslog**  
- Parsing text/CSV/JSON; persistence.  
- SNMP walks with `pysnmp`; syslog ingestion & summarization.  
- **Lab 03:** Observability mini‑pipeline (SNMP + syslog → health report).

**Day 3 — RESTful APIs for Network Automation**  
- REST fundamentals, auth, status codes, retries.  
- Cisco RESTCONF & Junos REST (with offline fixtures).  
- **Lab 04:** GET/PUT/PATCH/DELETE workflow; validate & rollback.

**Day 4 — Multi‑Vendor Config & Ansible**  
- Idempotent configuration at scale: Jinja2 templates, dry‑run/diffs/validation.  
- **Lab 05:** VLAN creation + interface descriptions across Cisco & Juniper; validate with NAPALM getters.  
- **Lab 06:** Reproduce in Ansible (inventory, variables, network modules, check mode/diffs).

**Day 5 — Capstone & Demos**  
- Change window design, guardrails, rollback plan.  
- **Capstone:** inventory → collect state (SNMP/API) → policy checks → execute multi‑vendor change (Python or Ansible) → capture diffs & evidence.
