import re
string = "I love Python"
pattern = "Python"
match = re.search(pattern, string)
if match:
	print(match.group())
