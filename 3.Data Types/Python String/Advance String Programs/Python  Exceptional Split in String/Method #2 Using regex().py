# Python3 code to demonstrate working of
# Exceptional Split in String
# Using regex()
import re

# initializing string
test_str = "gfg, is, (best, for), geeks"

# printing original string
print("The original string is : " + test_str)

# Exceptional Split in String
# Using regex()
res = re.split(r', (?!\S\)|\()', test_str)

# printing result
print("The string after exceptional split : " + str(res))
