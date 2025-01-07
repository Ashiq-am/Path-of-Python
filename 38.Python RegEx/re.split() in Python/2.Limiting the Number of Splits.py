import re

# Original string
s = "geeks for geeks gfg"

# Split the string by space, but limit the number of splits to 2
result = re.split(r"\s+", s, maxsplit=2)

print(result)