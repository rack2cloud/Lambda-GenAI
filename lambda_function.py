import json
import boto3
import base64

bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # 1. Decode log input
        log_input = base64.b64decode(event['body']).decode('utf-8') if event.get('isBase64Encoded') else event.get('body', '')
        
        # 2. Ultra-tight SRE prompt
        # Adding 'RCA:' at the end acts as a "completion trigger"
        prompt = f"<s>[INST] <<SYS>>\nYou are a concise SRE tool. Output ONLY a one-sentence root cause analysis. No yapping.\n<</SYS>>\n\nLog: {log_input} [/INST] RCA:"

        # 3. Payload with loop-prevention
        body = json.dumps({
            "prompt": prompt,
            "max_gen_len": 64,
            "temperature": 0.1,
            "top_p": 0.9,
            "stop_sequences": ["[INST]", "</s>", "\n", "Log:"] # This kills the repetition
        })

        # 4. Invoke Model
        response = bedrock.invoke_model(
            modelId='us-east-1:meta.llama3-2-1b-instruct-v1:0',
            body=body
        )

        # 5. Clean up response
        response_body = json.loads(response.get('body').read())
        generation = response_body.get('generation', '').strip()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': generation
        }

    except Exception as e:
        return {'statusCode': 500, 'body': f"Error: {str(e)}"}
