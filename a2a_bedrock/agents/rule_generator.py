def generate_rules_with_bedrock(bedrock_client, active_rule_ids, all_rules_config):
    """Generates the CloudFormation template for AWS Config rules using Bedrock."""
    
    prompt = "Create a single AWS CloudFormation template in YAML format. " \
             "The template should contain AWS::Config::ConfigRule resources for the following rules:\n\n"    
    for rule_id in active_rule_ids:
        if rule_id in all_rules_config:
            rule = all_rules_config[rule_id]
            prompt += f"- Rule ID: {rule_id}, Name: {rule.get('name')}, " \
                      f"Source Identifier: {rule.get('source_identifier')}, " \
                      f"Resource Type: {rule.get('resource_type')}, " \
                      f"Description: {rule.get('description')}\n"
            
    prompt += "\nPlease ensure the output is only the YAML code for the CloudFormation template."
    
    return bedrock_client.generate_content(prompt)