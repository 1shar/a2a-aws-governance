import yaml
from agents.guideline_parser import parse_guidelines
from agents.rule_generator import generate_rules, generate_standalone_rules
from agents.doc_generator import generate_docs
from agents.code_validator import validate_cfn_template
from agents.excel_generator import generate_excel_report

def main():
    """Orchestrator to run the A2A pipeline."""
    # Load configuration
    with open('a2a_governance/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    all_rules_config = config.get('rules', {})

    # 1. Guideline Parser Agent: Get the list of active rule IDs
    active_rule_ids = parse_guidelines('a2a_governance/guidelines/security_policies.md')

    # 2. Rule Generator Agent with Validation
    max_retries = 3
    for attempt in range(max_retries):
        cfn_template = generate_rules(active_rule_ids, all_rules_config, 'a2a_governance/templates/rule_template.j2')
        
        # Temporarily write to a file for validation
        temp_template_path = 'a2a_governance/output/temp_aws-config-rules.yaml'
        with open(temp_template_path, 'w') as f:
            f.write(cfn_template)

        # Validate the generated template
        if validate_cfn_template(temp_template_path):
            # If valid, move to the final output path
            import os
            os.rename(temp_template_path, 'a2a_governance/output/aws-config-rules.yaml')
            print("Successfully generated and validated CloudFormation template.")
            break
        else:
            print(f"Attempt {attempt + 1} failed. Retrying...")
            if attempt + 1 == max_retries:
                print("Failed to generate a valid CloudFormation template after several retries.")
                # Optionally, clean up the temporary file
                import os
                os.remove(temp_template_path)
                return  # Exit if all retries fail

    # 4. Standalone Rule Generator Agent
    standalone_templates = generate_standalone_rules(active_rule_ids, all_rules_config, 'a2a_governance/templates/standalone_rule_template.j2')
    for file_name, content in standalone_templates.items():
        with open(f'a2a_governance/output/standalone_rules/{file_name}', 'w') as f:
            f.write(content)
    print("Successfully generated standalone CloudFormation templates.")

    # 6. Excel Report Generator Agent
    generate_excel_report(active_rule_ids, all_rules_config, 'a2a_governance/output/aws-config-rules.xlsx')
    print("Successfully generated Excel report.")

if __name__ == "__main__":
    main()