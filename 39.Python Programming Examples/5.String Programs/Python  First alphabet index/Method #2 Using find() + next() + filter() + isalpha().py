# Python3 code to demonstrate working of
# First alphabet index
# Using find() + next() + filter() + isalpha()
import re

# initializing string
test_str = "34#$g67fg"

# printing original string
print("The original string is : " + test_str)

# First alphabet index
# Using find() + next() + filter() + isalpha()
res = test_str.find(next(filter(str.isalpha, test_str)))

# printing result
print("Index of first character : " + str(res))
