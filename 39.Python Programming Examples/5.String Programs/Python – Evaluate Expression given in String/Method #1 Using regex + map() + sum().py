# Python3 code to demonstrate working of
# Expression evalution in String
# Using regex + map() + sum()
import re

# initializing string
test_str = "45 + 98-10"

# printing original string
print("The original string is : " + test_str)

# Expression evalution in String
# Using regex + map() + sum()
res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))

# printing result
print("The evaluated result is : " + str(res))
