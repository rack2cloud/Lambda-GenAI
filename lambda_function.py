import boto3
import json
import os

# Deterministic Logic: Sub-500ms Cold Start focus
# This handler uses the Converse API for optimized throughput
def lambda_handler(event, context):
    try:
        # 1. Parse Input (Supports raw text or JSON)
        body = json.loads(event.get('body', '{}'))
        user_prompt = body.get('prompt', 'Hello Llama, are you awake?')

        # 2. Initialize Bedrock Runtime
        # Note: Boto3 handles the signature versioning for fast handshakes
        client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

        # 3. Invoke Llama 3.2 (Bedrock Model ID)
        model_id = "us.meta.llama3-2-1b-instruct-v1:0" 
        
        response = client.converse(
            modelId=model_id,
            messages=[{"role": "user", "content": [{"text": user_prompt}]}],
            inferenceConfig={"maxTokens": 512, "temperature": 0.5}
        )

        # 4. Extract and Return
        output_text = response['output']['message']['content'][0]['text']
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'response': output_text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
