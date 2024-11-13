# Python3 code to demonstrate working of
# Extract string till first Non-Alphanumeric character
# Using regex + search()
import re

# initializing string
test_str = 'geeks4g!!!eeks'

# printing original string
print("The original string is : " + str(test_str))

# using start() to get 1st substring
res = re.search(r'\W+', test_str).start()
res = test_str[0: res]

# printing result
print("The resultant string : " + str(res))
