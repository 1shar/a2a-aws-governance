import json

def lambda_handler(event, context):
    # This is a placeholder. In a real-world scenario, you would have logic
    # to track the number of IAM roles and flag if it exceeds a threshold.
    # For this example, we'll assume any new role creation is compliant
    # as the rule's purpose is to monitor, not prevent.
    
    invoking_event = json.loads(event["invokingEvent"])
    configuration_item = invoking_event["configurationItem"]
    
    evaluations = [
        {
            "ComplianceResourceType": configuration_item["resourceType"],
            "ComplianceResourceId": configuration_item["resourceId"],
            "ComplianceType": "COMPLIANT",
            "Annotation": "IAM role creation is being monitored.",
            "OrderingTimestamp": configuration_item["configurationItemCaptureTime"]
        }
    ]
    
    result_token = event["resultToken"]
    # Send the evaluation results to AWS Config
    # config.put_evaluations(Evaluations=evaluations, ResultToken=result_token)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Evaluation complete!')
    }
