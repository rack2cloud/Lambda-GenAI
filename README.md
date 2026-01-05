# Lambda-GenAI
Sub-500ms Cold Starts for Llama 3.2 on AWS Lambda using Amazon Bedrock.

# ⚡ AWS Lambda + Llama 3.2 (The Sub-500ms Cold Start PoC)

[![Aura Ops Live Utility](https://img.shields.io/badge/Live%20Utility-Aura%20Ops-blueviolet)](https://www.rack2cloud.com/aura-ops-utility/)
[![Maintained by Rack2Cloud](https://img.shields.io/badge/Maintained%20by-Rack2Cloud-blue)](https://www.rack2cloud.com)
[![Status](https://img.shields.io/badge/Update-Jan%205%2C%202026-orange)](#)

This repository provides a high-performance implementation for running Generative AI (Llama 3.2) on AWS Lambda. By offloading weight-paging to the Amazon Bedrock managed plane, we achieve near-instant initialization.

## 🛠 Aura Ops Diagnostic Engine (Status: Deploying Today Jan 5, 2026)
We are currently integrating the "Surgical Scraper" and Diagnostic Logic module (ETA 9:00 PM EST). 

### **Diagnostic Support Matrix (Jan 2026)**
| System | Log Source | Support Level | Focus Area |
| :--- | :--- | :--- | :--- |
| **Nutanix AOS** | `syslog` / `logbay` | Beta | Metadata (Cassandra), Data Path (Stargate) |
| **Pure Storage** | `purity//fa` alerts | Beta | Controller Redundancy, Path Latency |
| **VMware ESXi** | `vmkernel.log` | Planned | Resource Contention, SCSI locking |

---

## 📜 License
MIT - Created and maintained by the engineering team at [Rack2Cloud](https://www.rack2cloud.com).
