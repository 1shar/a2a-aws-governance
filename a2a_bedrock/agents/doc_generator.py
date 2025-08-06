def generate_docs_with_bedrock(bedrock_client, active_rule_ids, all_rules_config):
    """Generates the markdown documentation using Bedrock."""
    
    prompt = "Create a markdown document for the following AWS Config rules. " \
             "The document should have a main title, a summary table with Rule ID, Name, and Description, " \
             "and a detailed section for each rule with its ID, Name, Description, Rationale, and Remediation.\n\n"

    for rule_id in active_rule_ids:
        if rule_id in all_rules_config:
            rule = all_rules_config[rule_id]
            prompt += f"- Rule ID: {rule_id}, Name: {rule.get('name')}, " \
                      f"Description: {rule.get('description')}, " \
                      f"Rationale: {rule.get('rationale')}, " \
                      f"Remediation: {rule.get('remediation')}\n"

    prompt += "\nPlease ensure the output is a well-formatted markdown document."

    return bedrock_client.generate_content(prompt)