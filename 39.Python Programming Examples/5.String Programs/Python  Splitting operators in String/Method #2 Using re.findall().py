# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.findall()
import re

# initializing string
test_str = "15 + 22.6 * 3-4 / 2"

# printing original string
print("The original string is : " + str(test_str))

# Using re.findall()
# Splitting operators in String
res = re.findall(r'[0-9\.]+|[^0-9\.]+', test_str)

# printing result
print("The list after performing split functionality : " + str(res))
