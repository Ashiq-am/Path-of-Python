import re
s1 = "Python"

# Index of the character to remove
idx = 3

# Use regex to replace the character at the specified index
pattern = re.escape(s1[idx])
res = re.sub(pattern, "", s1, count=1)
print(res)