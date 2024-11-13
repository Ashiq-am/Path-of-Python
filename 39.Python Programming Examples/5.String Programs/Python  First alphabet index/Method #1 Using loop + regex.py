# Python3 code to demonstrate working of
# First alphabet index
# Using loop + regex
import re

# initializing string
test_str = "34#$g67fg"

# printing original string
print("The original string is : " + test_str)

# First alphabet index
# Using loop + regex
res = None
temp = re.search(r'[a-z]', test_str, re.I)
if temp is not None:
	res = temp.start()

# printing result
print("Index of first character : " + str(res))
