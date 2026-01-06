#!/bin/bash

ENDPOINT="https://jbbdggbjfb3rii2ijfpestjsmy0meqnq.lambda-url.us-east-1.on.aws/"

echo "🚀 Starting Aura Ops Validation Suite..."
echo "---------------------------------------"

# Test 1: Kubernetes Compute Error
echo "🧪 Test 1: Kubernetes Compute..."
curl -s -X POST $ENDPOINT -d "Warning Failed kubelet Failed to pull image 'nginxx:latest'" | jq .
echo -e "\n"

# Test 2: Pure Storage Error
echo "🧪 Test 2: Pure Storage CBT..."
curl -s -X POST $ENDPOINT -d "Error: Purity//FA reported CBT drift on volume 'vol-99' during snapshot" | jq .
echo -e "\n"

# Test 3: Nutanix Generic Alert
echo "🧪 Test 3: Nutanix Generic..."
curl -s -X POST $ENDPOINT -d "Critical: Nutanix Stargate service is reporting high metadata latency" | jq .
echo "---------------------------------------"
echo "✅ Validation Complete."
