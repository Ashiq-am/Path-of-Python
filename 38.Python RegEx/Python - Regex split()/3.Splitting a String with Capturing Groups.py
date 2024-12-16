import re
s = "Geeks, for; Geeks"

# Using split() with a capturing group to keep the delimiters
result = re.split(r'(,|;)', s)

print(result)