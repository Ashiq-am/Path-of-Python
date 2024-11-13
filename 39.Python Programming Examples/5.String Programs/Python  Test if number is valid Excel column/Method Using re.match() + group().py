# Python3 code to demonstrate working of
# Test if number is valid Excel column
# Using re.match() + groupby()
import re

# initializing string
test_str = "C101"

# printing original string
print("The original string is : " + test_str)

# Test if number is valid Excel column
# Using re.match() + groupby()
temp = re.match(r'^([A-Z]{1, 2}|[A-W][A-Z]{2}|X[A-E][A-Z]|XF[A-D])([1-9]\d{0, 6})$', test_str)
res = bool(temp) and int(temp.group(2)) < 1048577

# printing result
print("Is string valid excel column : " + str(res))
