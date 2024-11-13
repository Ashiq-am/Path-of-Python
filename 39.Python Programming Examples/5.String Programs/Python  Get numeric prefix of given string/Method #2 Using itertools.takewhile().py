# Python3 code to demonstrate working of
# Get numeric prefix of string
# Using itertools.takewhile()
from itertools import takewhile

# initializing string
test_str = "1234Geeks"

# printing original string
print("The original string is : " + test_str)

# Using itertools.takewhile()
# Get numeric prefix of string
res = ''.join(takewhile(str.isdigit, test_str))

# printing result
print("The prefix number at string : " + str(res))
