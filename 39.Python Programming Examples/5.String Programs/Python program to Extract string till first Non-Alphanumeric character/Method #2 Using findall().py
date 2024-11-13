# Python3 code to demonstrate working of
# Extract string till first Non-Alphanumeric character
# Using findall()
import re

# initializing string
test_str = 'geeks4g!!!eeks'

# printing original string
print("The original string is : " + str(test_str))

# using findall() to get all substrings
# 0th index gives 1st substring
res = re.findall("[\dA-Za-z]*", test_str)[0]

# printing result
print("The resultant string : " + str(res))
