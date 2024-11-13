# Python3 code to demonstrate working of
# First K consecutive digits in String
# Using regex()
import re

# initializing string
test_str = "geeks5geeks43isbest"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 2

# using regex() to solve problem
temp = re.search('\d{% s}'% K, test_str)
res = (temp.group(0) if temp else '')

# printing result
print("Required character digits : " + str(res))
