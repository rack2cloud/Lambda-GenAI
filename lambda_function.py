import json
import boto3
import base64

# Initialize the Bedrock client
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # 1. Extract the log data from the POST request
        if event.get('isBase64Encoded'):
            log_input = base64.b64decode(event['body']).decode('utf-8')
        else:
            log_input = event.get('body', '')

        if not log_input:
            return {'statusCode': 400, 'body': json.dumps('No log data received')}

        # 2. Construct the high-speed prompt
        # We use [INST] tags for Llama 3.2 1B
        prompt = f"<s>[INST] <<SYS>>\nYou are a senior SRE. Provide a 1-sentence root cause for this log error.\n<</SYS>>\n\nLog: {log_input} [/INST]"

        # 3. Configure the model payload with stop sequences to prevent loops
        body = json.dumps({
            "prompt": prompt,
            "max_gen_len": 128,
            "temperature": 0.1,  # Low temp for consistent technical RCA
            "top_p": 0.9,
            "stop_sequences": ["[INST]", "</s>", "\n\n"] 
        })

        # 4. Invoke the Llama 3.2 1B model
        response = bedrock.invoke_model(
            modelId='us-east-1:meta.llama3-2-1b-instruct-v1:0', # Standard Llama 3.2 1B
            body=body
        )

        # 5. Parse and return the result
        response_body = json.loads(response.get('body').read())
        generation = response_body.get('generation', '').strip()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': generation
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal Server Error: {str(e)}")
        }
