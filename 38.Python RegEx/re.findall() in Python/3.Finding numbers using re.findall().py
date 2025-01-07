import re

# Find all numbers in a string
text = "There are 12 apples, 5 bananas, and 300 oranges."

# \d+ matches one or more digits
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)