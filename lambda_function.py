import json
import boto3
import base64

def scrape_signal(text):
    # Filters for high-signal keywords to keep token counts tiny
    keywords = ['ERROR', 'FATAL', 'Warning', 'Failed', 'Status:', 'Node:', 'latency']
    lines = text.split('\n')
    signal = [l for l in lines if any(k.lower() in l.lower() for k in keywords)]
    return "\n".join(signal[:15])

def lambda_handler(event, context):
    # Extracting the body from the curl POST
    raw_body = event.get('body', '')
    if event.get('isBase64Encoded'):
        raw_body = base64.b64decode(raw_body).decode('utf-8')
    
    # Run the Surgical Scraper
    clean_log = scrape_signal(raw_body)
    
    # Connect to Bedrock
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    
    prompt = f"Analyze this infra log and provide a 1-sentence RCA and 1 CLI fix:\n{clean_log}"
    
    # Llama 3.2 1B Instruct format
    native_request = {
        "prompt": f"<s>[INST] {prompt} [/INST]",
        "max_gen_len": 128,
        "temperature": 0.1,
    }
    
    try:
        response = bedrock.invoke_model(
            modelId='us.meta.llama3-2-1b-instruct-v1:0',
            body=json.dumps(native_request)
        )
        model_response = json.loads(response.get('body').read())
        output_text = model_response.get('generation', 'No diagnosis generated.')
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': output_text
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
