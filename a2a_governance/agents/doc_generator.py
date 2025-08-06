from jinja2 import Template

def generate_docs(active_rule_ids, all_rules_config, template_path):
    """Generates the markdown documentation from the config data."""
    with open(template_path, 'r') as f:
        template = Template(f.read())
        
    # Filter the rules from the config that are present in the active list
    active_rules = []
    for rule_id in active_rule_ids:
        if rule_id in all_rules_config:
            rule_details = all_rules_config[rule_id]
            # Add the main ID to the details dictionary for the template
            rule_details['id'] = rule_id
            active_rules.append(rule_details)

    return template.render(rules=active_rules)