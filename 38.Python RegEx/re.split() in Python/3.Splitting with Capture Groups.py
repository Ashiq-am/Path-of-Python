import re

# Original string
s = "geeks123for456geeks"

# Split the string at numbers, keeping the numbers in the result
result = re.split(r"(\d+)", s)

print(result)