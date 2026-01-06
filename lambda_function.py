import json
import boto3
import base64

bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        log_input = base64.b64decode(event['body']).decode('utf-8') if event.get('isBase64Encoded') else event.get('body', '')
        
        # Converse API call
        response = bedrock.converse(
            modelId='us.meta.llama3-2-1b-instruct-v1:0',
            messages=[{"role": "user", "content": [{"text": f"RCA this log: {log_input}"}]}],
            system=[{"text": "You are a senior SRE. Output ONLY a 1-sentence RCA."}],
            inferenceConfig={"maxTokens": 64, "temperature": 0.0}
        )

        rca_text = response['output']['message']['content'][0]['text'].strip()

        # Aura Ops Logic: Structured Data
        severity = "High" if "Failed" in log_input else "Medium"
        
        aura_output = {
            "rca": rca_text,
            "severity": severity,
            "source": "Surgical-Scraper-v1",
            "suggested_action": "Check image spelling or registry permissions."
        }
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(aura_output)
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({"error": str(e)})}
