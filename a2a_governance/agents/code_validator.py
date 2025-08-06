import logging
import cfnlint.core
import cfnlint.decode
import cfnlint.runner

def validate_cfn_template(template_path):
    """Validates a CloudFormation template using cfn-lint programmatically."""
    try:
        # Use the main decode function which handles both YAML and JSON
        # It returns the template and any decoding errors (matches)
        template, matches = cfnlint.decode.decode(template_path)

        # Check if there were any errors just loading/parsing the file
        if matches:
            error_messages = "\n".join([str(e) for e in matches])
            logging.error(f"CloudFormation template is malformed:\n{error_messages}")
            return False

        # Get default rules from cfn-lint
        rules = cfnlint.core.get_rules([], [], [])
        
        # Create a runner
        runner = cfnlint.runner.Runner(rules, template, template_path, None)
        
        # Run the validation
        errors = runner.run()
        
        if not errors:
            logging.info("CloudFormation template is valid.")
            return True
        else:
            # Join all error messages for detailed logging
            error_messages = "\n".join([str(e) for e in errors])
            logging.error(f"CloudFormation template validation failed:\n{error_messages}")
            return False
            
    except Exception as e:
        # Catch potential parsing errors or other issues during validation
        logging.error(f"An unexpected error occurred during cfn-lint validation: {e}")
        return False
