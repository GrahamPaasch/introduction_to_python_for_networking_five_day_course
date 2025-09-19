# GNS3 Integration (Instructor)

- **Purpose:** Document your running campus topology so students recognize what they see.
- **Add screenshots:** Save diagrams to `docs/assets/gns3/` and link them below.
- **Connectivity:** Confirm `lab.grahampaasch.com` reachability from student VMs and note any VPN steps.
- **Out-of-band admin:** Note credentials/roles and where students can safely test.

## Topology
![GNS3 Topology](assets/gns3/topology.png) <!-- Replace with your actual file -->

## Device Map (example)
| Hostname | Platform        | Mgmt IP    | Notes |
|----------|------------------|------------|-------|
| r1       | cisco_ios        | 10.0.0.11  | Core  |
| r2       | cisco_ios        | 10.0.0.12  | Edge  |
| j1       | juniper_junos    | 10.0.0.21  | Dist  |

## Student Access
- Portal: `lab.grahampaasch.com`  
- Accounts: pre-provisioned; test one student account before class.  
- Timeouts/quotas: note any session limits.

## Known Quirks
- Serial console flakiness on first connect — retry once before escalating.
- RESTCONF on Cisco may need `ip http secure-server` and `restconf` enabled.
