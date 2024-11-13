# importing regex
import re

# lookahead example
example = re.search(r'geeks(?=[a-z])', "geeksforgeeks")

# display output
print("Pattern:", example.group())
print("Pattern found from index:",
	example.start(), "to",
	example.end())
