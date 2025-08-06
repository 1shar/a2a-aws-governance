from jinja2 import Template

def generate_rules(active_rule_ids, all_rules_config, template_path):
    """Generates the CloudFormation template for AWS Config rules."""
    with open(template_path, 'r') as f:
        template = Template(f.read())
    
    active_rules = []
    for rule_id in active_rule_ids:
        if rule_id in all_rules_config:
            rule_details = all_rules_config[rule_id]
            rule_details['id'] = rule_id
            active_rules.append(rule_details)
            
    return template.render(rules=active_rules)

def generate_standalone_rules(active_rule_ids, all_rules_config, template_path):
    """Generates standalone CloudFormation templates for each rule."""
    with open(template_path, 'r') as f:
        template = Template(f.read())
    
    standalone_templates = {}
    for rule_id in active_rule_ids:
        if rule_id in all_rules_config:
            rule_details = all_rules_config[rule_id]
            rule_details['id'] = rule_id
            
            # Adjust source for template rendering
            rule_details_for_template = rule_details.copy()
            rule_details_for_template['source'] = {
                'owner': rule_details.get('source_owner', 'AWS'),
                'identifier': rule_details['source_identifier']
            }

            rendered_template = template.render(rule=rule_details_for_template)
            standalone_templates[f"{rule_id}-{rule_details['name']}.yaml"] = rendered_template
            
    return standalone_templates