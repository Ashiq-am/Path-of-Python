import re

t = "Hello, welcome to the world of Python."
pattern = "welcome"

# Search for the pattern in the text
result = re.search(pattern, t)

if result:
    print("Pattern found")
else:
    print("Pattern not found")