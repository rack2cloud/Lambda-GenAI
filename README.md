# Lambda-GenAI
Sub-500ms Cold Starts for Llama 3.2 on AWS Lambda using Amazon Bedrock.

# ⚡ AWS Lambda + Llama 3.2 (The Sub-500ms Cold Start PoC)

This repository provides a high-performance implementation for running Generative AI (Llama 3.2) on AWS Lambda. By offloading weight-paging to the Amazon Bedrock managed plane, we achieve near-instant initialization, bypassing the traditional 10s+ "Cold Start" penalty.

## 🛠 Aura Ops Diagnostic Engine (Coming 9 PM EST)
We are currently integrating a specialized module designed for "Zero-Fluff" root cause analysis of hybrid-cloud infrastructure logs.

### **Diagnostic Support Matrix**
| System | Log Source | Support Level | Focus Area |
| :--- | :--- | :--- | :--- |
| **Nutanix AOS** | `syslog` / `logbay` | Beta | Metadata (Cassandra), Data Path (Stargate) |
| **Pure Storage** | `purity//fa` alerts | Beta | Controller Redundancy, Path Latency |
| **VMware ESXi** | `vmkernel.log` | Planned | Resource Contention, SCSI locking |
| **Networking** | Generic Syslog | Alpha | MTU Mismatches, LACP/Port Channel |

### **How it works**
1. **Surgical Scraping:** The Lambda pre-processes logs to strip noise and timestamps, saving tokens and improving inference accuracy.
2. **Context Mapping:** Error strings are mapped to specific infrastructure "Identity Prompts" before being sent to Llama 3.2.
3. **Deterministic Output:** Returns a structured RCA (Root Cause Analysis) and a specific remediation CLI command.

## 🚀 Deployment
1. **Permissions:** Attach an IAM policy with `bedrock:InvokeModel` to your Lambda execution role.
2. **Settings:** Recommended memory: 3008MB (for optimized CPU allocation).
3. **Region:** Currently tested in `us-east-1`.

## 📜 License
MIT - Created by the team at [Rack2Cloud](https://www.rack2cloud.com).
