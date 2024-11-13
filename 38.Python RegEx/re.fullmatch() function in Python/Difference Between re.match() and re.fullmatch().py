import re


string = "Geeks for geeks"
pattern = "Geeks"

print(re.match(pattern, string))
print(re.fullmatch(pattern, string))
