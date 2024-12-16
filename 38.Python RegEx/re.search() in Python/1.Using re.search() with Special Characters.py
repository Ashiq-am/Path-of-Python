import re

a = "I have 2 apples and 10 oranges."
pattern = r"\d+"  # Pattern to match one or more digits

# Search for the pattern in the text
result = re.search(pattern, a)

if result:
    print("First number found:", result.group())
else:
    print("Pattern not found")