import re


# pattern is a string containing the regex pattern
pattern = r"[.*"

try:
	re.compile(pattern)

except re.error:
	print("Non valid regex pattern")
	exit()
