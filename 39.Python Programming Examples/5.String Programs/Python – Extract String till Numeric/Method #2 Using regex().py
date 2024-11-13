# Python3 code to demonstrate working of
# Extract String till Numeric
# Using regex()
import re

# initializing string
test_str = "geeks4geeks is best"

# printing original string
print("The original string is : " + str(test_str))

# regex to get all elements before numerics
res = re.findall('([a-zA-Z ]*)\d*.*', test_str)

# printing result
print("Extracted String : " + str(res[0]))
