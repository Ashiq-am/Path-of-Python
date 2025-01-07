import re

# Compile the pattern
pattern = re.compile(r'\d+')

# Search for digits in a string
result = pattern.search("I have 3 cats.")

if result:
    print(result.group())