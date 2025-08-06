import logging
import cfnlint.core
import cfnlint.decode

def validate_cfn_template(template_path):
    """Validates a CloudFormation template using cfn-lint's core run_checks function."""
    try:
        # Decode the template, which also checks for basic syntax errors
        (template, matches) = cfnlint.decode.decode(template_path)
        if matches:
            error_messages = "\n".join([str(m) for m in matches])
            logging.error(f"CloudFormation template is malformed:\n{error_messages}")
            return False

        # Get the default rule set
        rules = cfnlint.core.get_rules([], [], [])
        
        # Specify regions to lint against, us-east-1 is a safe default
        regions = ['us-east-1']
        
        # Run the checks using the core function
        errors = cfnlint.core.run_checks(
            filename=template_path,
            template=template,
            rules=rules,
            regions=regions
        )

        if not errors:
            logging.info("CloudFormation template is valid.")
            return True
        else:
            error_messages = "\n".join([str(e) for e in errors])
            logging.error(f"CloudFormation template validation failed:\n{error_messages}")
            return False
            
    except Exception as e:
        logging.error(f"An unexpected error occurred during cfn-lint validation: {e}")
        return False