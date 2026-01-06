import json
import boto3
import base64

# Use the Bedrock Runtime client
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # 1. Grab the log
        log_input = base64.b64decode(event['body']).decode('utf-8') if event.get('isBase64Encoded') else event.get('body', '')
        
        # 2. Use the Converse API (much more stable for Llama 3.2)
        # This removes the need for manual [INST] tags
        messages = [{
            "role": "user",
            "content": [{"text": f"Provide a one-sentence root cause analysis for this log: {log_input}"}]
        }]
        
        system_prompts = [{"text": "You are a concise SRE diagnostic tool. Output ONLY the RCA sentence."}]

        # 3. Request completion
        response = bedrock.converse(
            modelId='us-east-1:meta.llama3-2-1b-instruct-v1:0',
            messages=messages,
            system=system_prompts,
            inferenceConfig={"maxTokens": 64, "temperature": 0.0} # Zero temp for precision
        )

        # 4. Extract the clean text
        generation = response['output']['message']['content'][0]['text'].strip()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': generation
        }

    except Exception as e:
        return {'statusCode': 500, 'body': f"Error: {str(e)}"}
