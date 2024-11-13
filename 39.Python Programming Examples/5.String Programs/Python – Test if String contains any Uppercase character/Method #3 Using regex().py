# Python3 code to demonstrate working of
# Test if String contains any Uppercase character
# Using re()
import re

# initializing string
test_str = 'geeksforGeeks'

# printing original string
print("The original string is : " + str(test_str))

# Using regex to check for any element to be uppercase
res = bool(re.match(r'\w*[A-Z]\w*', test_str))

# printing result
print("Does String contain uppercase character : " + str(res))
