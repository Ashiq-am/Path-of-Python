# Python3 code to demonstrate working of
# Custom Split Comma Separated Words
# Using re.findall()
import re

# initializing string
test_str = 'geeksforgeeks, is, best, for, geeks'

# printing original string
print("The original string is : " + str(test_str))

# Distance between occurrences
# Using re.findall()
res = re.findall(r'\w+|\S', test_str)

# printing result
print("The strings after performing splits : " + str(res))
