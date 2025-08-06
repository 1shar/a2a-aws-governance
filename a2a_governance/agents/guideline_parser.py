import re

def parse_guidelines(file_path):
    """Parses the security guidelines to get a list of active rule IDs, handling various formats."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # This regex is more robust. It looks for lines starting with 'AWS', 
    # optionally followed by a space or hyphen, then captures the number and optional letter.
    # It allows for other text to exist on the line.
    # Example matches: "AWS-01", "AWS 23", "AWS-23a ..."
    matches = re.findall(r'^AWS[- ]?(\d+[a-z]?)', content, re.MULTILINE)
    
    # Reconstruct the standard ID format, e.g., "AWS-1", "AWS-23a"
    active_rule_ids = [f"AWS-{match}" for match in matches]
    
    return active_rule_ids
