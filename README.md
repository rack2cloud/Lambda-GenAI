# Lambda-GenAI
Sub-500ms Cold Starts for Llama 3.2 on AWS Lambda using Amazon Bedrock.

# ⚡ AWS Lambda + Llama 3.2 (The Sub-500ms Cold Start PoC)

### Why this exists
Standard LLM deployments on Lambda usually suffer from 10s+ cold starts because of model weight paging. This PoC offloads that heavy lifting to the Amazon Bedrock managed plane, allowing for near-instant initialization.

### Current Logic
- **Architecture:** API Gateway -> Lambda -> Bedrock (Converse API).
- **Latency:** Sub-500ms for initialization logic.
- **Cost:** Practically $0/mo on the AWS Free Tier for low-volume testing.

### Deployment Notes
- **IAM:** Ensure your execution role has `bedrock:InvokeModel` permissions.
- **Model:** Currently tuned for Llama 3.2 1B/3B (instruct).
- **Tonight's Update:** I'm integrating the 'Aura Ops' Diagnostic Engine into this repo at 9 PM EST to show how to use this for real-world Nutanix/Pure Storage log analysis.

*Part of the Rack2Cloud Engineering Workbench.*
