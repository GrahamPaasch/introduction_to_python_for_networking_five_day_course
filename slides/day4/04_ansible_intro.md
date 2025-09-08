---
marp: true
title: Day 4 — Ansible Intro
paginate: true
---

# Ansible Introduction

- Inventories & variables
- Network modules
- Check mode & diffs

---

## Why Ansible Here?

- Idempotent modules for common tasks
- Consistent inventory & vars
- Diffs and check mode for safety

---

## Collections

- `community.network`, `cisco.ios`, `junipernetworks.junos`
- Install: `ansible-galaxy collection install -r ansible/requirements.yml`

---

## Example Playbook

```yaml
- hosts: all
  gather_facts: no
  tasks:
    - cisco.ios.ios_vlans:
        config: [{ vlan_id: 123, name: TRAINING_VLAN }]
        state: merged
```

---

## Validation

- `--syntax-check` then `--check`
- Second run shows `changed=0`

---

## Hand‑Off from Python

- Build host vars/inventory in Python
- Invoke Ansible for standardized config

