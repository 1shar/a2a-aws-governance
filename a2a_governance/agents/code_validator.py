import subprocess
import logging

def validate_cfn_template(template_path):
    """Validates a CloudFormation template using cfn-lint."""
    try:
        subprocess.run(
            ['python', '-m', 'cfnlint', template_path],
            check=True,
            capture_output=True,
            text=True
        )
        logging.info("CloudFormation template is valid.")
        return True
    except FileNotFoundError:
        logging.error("'cfn-lint' not found. Please install it using 'pip install cfn-lint'.")
        return False
    except subprocess.CalledProcessError as e:
        logging.error(f"CloudFormation template validation failed:\nSTDOUT:\n{e.stdout}\nSTDERR:\n{e.stderr}")
        return False
