import json
import boto3
import base64

# Simple 'Surgical Scraper' inside the handler for speed
def scrape_signal(text):
    # Keep only lines with high-signal keywords to save tokens
    keywords = ['ERROR', 'FATAL', 'Warning', 'Failed', 'Status:', 'Node:']
    lines = text.split('\n')
    signal = [l for l in lines if any(k in l for k in keywords)]
    return "\n".join(signal[:15]) # Limit to top 15 matches

def lambda_handler(event, context):
    # 1. Extract the raw log from the curl command
    raw_body = event.get('body', '')
    
    # Handle base64 encoding (common in API Gateway/Lambda handshake)
    if event.get('isBase64Encoded'):
        raw_body = base64.b64decode(raw_body).decode('utf-8')
    
    # 2. Scrape for signal
    clean_log = scrape_signal(raw_body)
    
    # 3. Invoke Bedrock (Llama 3.2)
    bedrock = boto3.client(service_name='bedrock-runtime')
    
    prompt = f"Analyze this infrastructure log and provide a 1-sentence RCA and 1 CLI command to fix it:\n{clean_log}"
    
    body = json.dumps({
        "prompt": f"<s>[INST] {prompt} [/INST]",
        "max_gen_len": 128,
        "temperature": 0.1
    })
    
    response = bedrock.invoke_model(
        modelId='us.meta.llama3-2-1b-instruct-v1:0', # Using the lean 1B for speed
        body=body
    )
    
    result = json.loads(response.get('body').read())
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'body': result.get('generation')
    }
