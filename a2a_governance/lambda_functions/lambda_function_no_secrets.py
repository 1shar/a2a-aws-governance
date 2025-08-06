import json
import re

def lambda_handler(event, context):
    invoking_event = json.loads(event["invokingEvent"])
    configuration_item = invoking_event["configurationItem"]
    function_name = configuration_item["resourceName"]
    
    # In a real-world scenario, you would download and inspect the function code.
    # This is a simplified check based on environment variables.
    environment_variables = configuration_item.get('configuration', {}).get('environment', {}).get('variables', {})
    
    compliance_type = 'COMPLIANT'
    annotation = 'No hardcoded secrets found in environment variables.'
    
    for key, value in environment_variables.items():
        if re.search(r'SECRET|PASSWORD|API_KEY', key, re.IGNORECASE):
            compliance_type = 'NON_COMPLIANT'
            annotation = f'Potential secret found in environment variable: {key}'
            break

    evaluations = [
        {
            "ComplianceResourceType": configuration_item["resourceType"],
            "ComplianceResourceId": function_name,
            "ComplianceType": compliance_type,
            "Annotation": annotation,
            "OrderingTimestamp": configuration_item["configurationItemCaptureTime"]
        }
    ]
    
    # config.put_evaluations(Evaluations=evaluations, ResultToken=event["resultToken"])
    return {
        'statusCode': 200,
        'body': json.dumps('Evaluation complete!')
    }