# Python3 code to demonstrate working of
# Uppercase Selective Substrings in String
# Using re.sub() + upper()
import re

# initializing strings
test_str = 'geeksforgeeks is best for cs'

# printing original string
print("The original string is : " + str(test_str))

# initializing substrings
sub_list = ["best", "cs", "geeksforgeeks"]

# constructing regex
reg = '|'.join(sub_list)
res = re.sub(reg, lambda ele: ele.group(0).upper(), test_str)

# printing result
print("The String after uppercasing : " + str(res))
