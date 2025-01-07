import re

# Original string
s = "geeks,for;geeks gfg"

# Split the string by commas, semicolons, or spaces
result = re.split(r"[,\s;]+", s)

print(result)