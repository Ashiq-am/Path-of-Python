import re

# Original string
s = "Geeks for Geeks"

# Replace 'cats' with 'dogs'
new_s, count = re.subn("nerds", "geeks", s)

print(new_s)
print("Replacements made:", count)