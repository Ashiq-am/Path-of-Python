# Python3 code to demonstrate working of
# Test if string contains both Numbers and Alphabets only
# Using regex
import re

# initializing string
test_str = 'Geeks4Geeks'

# printing original string
print("The original string is : " + str(test_str))

# conditional combination for getting result.
res = bool(re.match("^(?=.*[a-zA-Z])(?=.*[\d])[a-zA-Z\d]+$", "A530"))

# printing result
print("Does string contain both numbers and alphabets only? : " + str(res))
