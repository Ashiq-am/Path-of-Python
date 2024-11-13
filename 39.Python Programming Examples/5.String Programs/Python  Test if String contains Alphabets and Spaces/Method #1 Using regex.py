# Python3 code to demonstrate working of
# Test if String contains Alphabets and Spaces
# Using regex
import re

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + test_str)

# Test if String contains Alphabets and Spaces
# Using regex
res = bool(re.match('[a-zA-Z\s]+$', test_str))

# printing result
print("Does String contain only space and alphabets : " + str(res))
