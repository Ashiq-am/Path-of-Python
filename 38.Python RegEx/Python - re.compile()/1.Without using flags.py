import re

# Compile a regex pattern
pattern = re.compile(r'\d{3}-\d{2}-\d{4}')

# Use the compiled pattern to match
text = "My SSN is 123-45-6789."

match = pattern.search(text)
if match:
    print(f"Found: {match.group()}")