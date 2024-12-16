import re

a = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern to match phone number

# Search for the pattern in the text
result = re.search(pattern, a)

if result:
    print("Phone number found:", result.group())  # Extract the matched phone number
    print("Match starts at position:", result.start())
else:
    print("Pattern not found")