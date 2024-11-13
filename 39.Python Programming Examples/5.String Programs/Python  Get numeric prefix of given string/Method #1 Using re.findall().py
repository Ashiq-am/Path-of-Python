# Python3 code to demonstrate working of
# Get numeric prefix of string
# Using re.findall()
import re

# initializing string
test_str = "1234Geeks"

# printing original string
print("The original string is : " + test_str)

# Using re.findall()
# Get numeric prefix of string
res = re.findall('\d+', test_str)

# printing result
print("The prefix number at string : " + str(res[0]))
