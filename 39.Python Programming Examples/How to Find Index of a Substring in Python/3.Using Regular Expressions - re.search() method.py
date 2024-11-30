import re

s = "Hello, Geeks for geeks"

# searching for string 'geeks'
res = re.search(r"geeks", s)

# printing starting index of string
print(res.start())