# Lambda-GenAI
Sub-500ms Cold Starts for Llama 3.2 on AWS Lambda using Amazon Bedrock.

# Lambda-GenAI
Sub-500ms Cold Starts for Llama 3.2 on AWS Lambda using Amazon Bedrock.

# ⚡ AWS Lambda + Llama 3.2 (The Sub-500ms Cold Start PoC)

[![Aura Ops Live Utility](https://img.shields.io/badge/Live%20Utility-Aura%20Ops-blueviolet)](https://www.rack2cloud.com/aura-ops-utility/)
[![Maintained by Rack2Cloud](https://img.shields.io/badge/Maintained%20by-Rack2Cloud-blue)](https://www.rack2cloud.com)
[![Status](https://img.shields.io/badge/Update-Jan%206%2C%202026-orange)](#)

This repository provides a high-performance implementation for running Generative AI (Llama 3.2) on AWS Lambda. By offloading weight-paging to the Amazon Bedrock managed plane, we achieve near-instant initialization, bypassing the traditional 10s+ "Cold Start" penalty.

---

## 🛠 Aura Ops Diagnostic Engine (Status: Stable / Production-Ready)
We have successfully integrated the **"Surgical Scraper"** module using the **Amazon Bedrock Converse API**. This architecture uses **Inference Profiles** to ensure sub-500ms Root Cause Analysis (RCA) without the token-looping issues found in standard LLM implementations.

### **Diagnostic Support Matrix**
| System | Log Source | Support Level | Focus Area |
| :--- | :--- | :--- | :--- |
| **Nutanix AOS** | `syslog` / `logbay` | Beta | Metadata (Cassandra), Data Path (Stargate) |
| **Pure Storage** | `purity//fa` alerts | **Active** | CBT Drift, Controller Redundancy, Path Latency |
| **Kubernetes** | `kubectl describe` | **Active** | ImagePullBackOff, Node Affinity, OOMKills |
| **VMware ESXi** | `vmkernel.log` | Planned | Resource Contention, SCSI locking |

---

## 🚀 CLI Integration: The "Surgical" Diagnostic
You can pipe cluster outputs directly into the engine for a sub-500ms RCA.

**Test the live endpoint with a simple curl:**
```bash
curl -X POST [https://jbbdggbjfb3rii2ijfpestjsmy0meqnq.lambda-url.us-east-1.on.aws/](https://jbbdggbjfb3rii2ijfpestjsmy0meqnq.lambda-url.us-east-1.on.aws/) \
  -H "Content-Type: text/plain" \
  -d "Warning Failed kubelet Failed to pull image 'nginxx:latest'"
```
## Expected Response
```bash
{
  "rca": "The root cause is a typo in the container image name 'nginxx'.",
  "severity": "High",
  "source": "Surgical-Scraper-v1",
  "suggested_action": "Check image spelling or registry permissions."
}
```
## 🏗 Why this exists
In 2026, the shift toward **Sovereign Infrastructure** means we have to care about the substrate again. Managing disaggregated Nutanix + Pure stacks shouldn't mean jumping between three different consoles. This project is the open-source core of our mission to bring "Prism-simplicity" to the entire hybrid-cloud stack.

## 🚀 Deployment
1. **Permissions:** Attach an IAM policy with `bedrock:Converse` to your Lambda execution role.
2. **Inference Profile:** Uses `us.meta.llama3-2-1b-instruct-v1:0` for cross-region stability.
3. **Settings:** Recommended memory: **512MB**.

## 📜 License
MIT - Created and maintained by the engineering team at [Rack2Cloud](https://www.rack2cloud.com).



