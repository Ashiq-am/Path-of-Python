# Python3 code to demonstrate working of
# Splitting text and number in string
# Using re.compile() + re.match() + re.groups()
import re

# initializing string
test_str = "Geeks4321"

# printing original string
print("The original string is : " + str(test_str))

# Using re.compile() + re.match() + re.groups()
# Splitting text and number in string
temp = re.compile("([a-zA-Z]+)([0-9]+)")
res = temp.match(test_str).groups()

# printing result
print("The tuple after the split of string and number : " + str(res))
