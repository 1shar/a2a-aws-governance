import boto3
import json

class BedrockClient:
    def __init__(self, model_id):
        self.model_id = model_id
        self.client = boto3.client(service_name='bedrock-runtime')

    def generate_content(self, prompt):
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "user",
                    "content": [{ "type": "text", "text": prompt}]
                }
            ]
        })

        response = self.client.invoke_model(
            body=body, 
            modelId=self.model_id, 
            accept='application/json', 
            contentType='application/json'
        )
        
        response_body = json.loads(response.get('body').read())
        return response_body.get('content', [{}])[0].get('text', '')
