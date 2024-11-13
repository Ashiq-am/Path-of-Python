# Python3 code to demonstrate working of
# Extract substrings between brackets
# Using regex
import re

# initializing string
test_str = "geeks(for)geeks is (best)"

# printing original string
print("The original string is : " + test_str)

# Extract substrings between brackets
# Using regex
res = re.findall(r'\(.*?\)', test_str)

# printing result
print("The element between brackets : " + str(res))
