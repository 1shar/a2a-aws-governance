import yaml
from agents.guideline_parser import parse_guidelines
from agents.rule_generator import generate_rules_with_bedrock
from agents.doc_generator import generate_docs_with_bedrock
from agents.code_validator import validate_cfn_template
from agents.excel_generator import generate_excel_report
from agents.bedrock_client import BedrockClient

def main():
    """Orchestrator to run the A2A Bedrock pipeline."""
    # Load configuration
    with open('a2a_bedrock/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    all_rules_config = config.get('rules', {})
    bedrock_config = config.get('bedrock', {})
    bedrock_client = BedrockClient(model_id=bedrock_config.get('model_id'))

    # 1. Guideline Parser Agent: Get the list of active rule IDs
    active_rule_ids = parse_guidelines('a2a_bedrock/guidelines/security_policies.md')

    # 2. Rule Generator Agent with Bedrock and Validation
    max_retries = 3
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} to generate CloudFormation template with Bedrock...")
        cfn_template = generate_rules_with_bedrock(bedrock_client, active_rule_ids, all_rules_config)
        
        temp_template_path = 'a2a_bedrock/output/temp_aws-config-rules.yaml'
        with open(temp_template_path, 'w') as f:
            f.write(cfn_template)

        if validate_cfn_template(temp_template_path):
            import os
            os.rename(temp_template_path, 'a2a_bedrock/output/aws-config-rules.yaml')
            print("Successfully generated and validated CloudFormation template with Bedrock.")
            break
        else:
            if attempt + 1 == max_retries:
                print("Failed to generate a valid CloudFormation template with Bedrock after several retries.")
                import os
                os.remove(temp_template_path)
                return

    # 3. Documentation Generator Agent with Bedrock
    print("Generating Markdown documentation with Bedrock...")
    markdown_doc = generate_docs_with_bedrock(bedrock_client, active_rule_ids, all_rules_config)
    with open('a2a_bedrock/output/aws-config-rules.md', 'w') as f:
        f.write(markdown_doc)
    print("Successfully generated Markdown documentation with Bedrock.")

    # 4. Excel Report Generator Agent
    generate_excel_report(active_rule_ids, all_rules_config, 'a2a_bedrock/output/aws-config-rules.xlsx')
    print("Successfully generated Excel report.")

if __name__ == "__main__":
    main()