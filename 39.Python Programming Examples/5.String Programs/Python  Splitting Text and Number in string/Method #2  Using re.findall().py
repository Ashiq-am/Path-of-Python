# Python3 code to demonstrate working of
# Splitting text and number in string
# Using re.findall()
import re

# initializing string
test_str = "Geeks4321"

# printing original string
print("The original string is : " + str(test_str))

# Using re.findall()
# Splitting text and number in string
res = [re.findall(r'(\w+?)(\d+)', test_str)[0] ]

# printing result
print("The tuple after the split of string and number : " + str(res))
