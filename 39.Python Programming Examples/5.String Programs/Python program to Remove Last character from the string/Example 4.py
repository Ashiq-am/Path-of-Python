import re

def reg(m):
	return m.group(1)

# sample string
Str = "GEEKSFORGEEKS"

# Remove last character from string
new_string = re.sub("(.*)(.{1}$)", reg, Str)
print(new_string)
