# Python3 code to demonstrate working of
# Check for spaces in string
# Using regex
import re

# initializing string
test_str = "Geeks forGeeks"

# printing original string
print("The original string is : " + test_str)

# Using regex
# Check for spaces
res = bool(re.search(r"\s", test_str))

# printing result
print("Does string contain spaces ? " + str(res))
