# Python3 code to demonstrate working of
# Check Numeric Suffix in String
# Using regex
import re

# initializing string
test_str = "Geeks4321"

# printing original string
print("The original string is : " + str(test_str))

# Using regex
# Check Numeric Suffix in String
res = re.search(r'\d+$', test_str)

# printing result
print("Does string contain suffix number ? : " + str(bool(res)))
