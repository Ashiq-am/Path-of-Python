import re

# Compile a case-insensitive regex
pattern = re.compile(r'hello', re.IGNORECASE)

# Use the compiled pattern
text = "Hello, GeeksforGeeks!"

match = pattern.search(text)
if match:
    print(f" {match.group()}")