# Python3 code to demonstrate working of
# Extract Suffix numbers
# Using regex
import re

# initializing string
test_str = "GFG04"

# printing original string
print("The original string is : " + str(test_str))

# regex to extract number
res = re.search(r"(\d+)$", test_str).group()

# printing result
print("Suffix number : " + str(res))
