import json
import boto3
import base64

bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        log_input = base64.b64decode(event['body']).decode('utf-8') if event.get('isBase64Encoded') else event.get('body', '')
        
        # New "Instruction-First" Prompt to kill the loop
        prompt = f"Instruction: Provide a one-sentence RCA for this log.\nLog: {log_input}\nRCA:"

        body = json.dumps({
            "prompt": prompt,
            "max_gen_len": 64,
            "temperature": 0, # Set to 0 for maximum technical precision
            "top_p": 0.1,
            "stop_sequences": ["\n", "Log:", "Instruction:"] # Force-kill any repetition
        })

        response = bedrock.invoke_model(
            modelId='us-east-1:meta.llama3-2-1b-instruct-v1:0',
            body=body
        )

        response_body = json.loads(response.get('body').read())
        # Strip any leading whitespace or tags
        generation = response_body.get('generation', '').split('RCA:')[-1].strip()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': generation
        }

    except Exception as e:
        return {'statusCode': 500, 'body': f"Error: {str(e)}"}
