import json
import boto3

iam_client = boto3.client('iam')

def lambda_handler(event, context):
    invoking_event = json.loads(event["invokingEvent"])
    configuration_item = invoking_event["configurationItem"]
    policy_arn = configuration_item["ARN"]

    # Get the default policy version
    policy = iam_client.get_policy(PolicyArn=policy_arn)['Policy']
    policy_version = iam_client.get_policy_version(
        PolicyArn=policy_arn, 
        VersionId=policy['DefaultVersionId']
    )['PolicyVersion']

    policy_document = policy_version['Document']
    
    compliance_type = 'COMPLIANT'
    annotation = 'No broad Bedrock access found.'

    for statement in policy_document.get('Statement', []):
        if (statement.get('Effect') == 'Allow' and 
            statement.get('Action') == 'bedrock:*'):
            compliance_type = 'NON_COMPLIANT'
            annotation = 'This policy grants full access to Bedrock.'
            break

    evaluations = [
        {
            "ComplianceResourceType": configuration_item["resourceType"],
            "ComplianceResourceId": configuration_item["resourceId"],
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