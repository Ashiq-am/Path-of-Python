# Python3 code to demonstrate working of
# Wildcard Substring search
# Using re.finditer()
import re

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Substring
sub_str = '..st'

# Wildcard Substring search
# Using re.finditer()
temp = re.compile(sub_str)
res = temp.search(test_str)

# printing result
print("The substring match is : " + str(res.group(0)))
