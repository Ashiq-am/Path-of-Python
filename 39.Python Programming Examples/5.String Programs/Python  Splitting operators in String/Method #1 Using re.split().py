# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.split()
import re

# initializing string
test_str = "15 + 22 * 3-4 / 2"

# printing original string
print("The original string is : " + str(test_str))

# Using re.split()
# Splitting operators in String
res = re.split(r'(\D)', test_str)

# printing result
print("The list after performing split functionality : " + str(res))
