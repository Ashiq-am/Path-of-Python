# Python3 code to demonstrate working of
# Extract Numbers in Brackets in String
# Using regex
import re

# initializing string
test_str = "gfg is [1] [4] all geeks"

# printing original string
print("The original string is : " + test_str)

# Extract Numbers in Brackets in String
# Using regex
res = re.findall(r"\[\s*\+?(-?\d+)\s*\]", test_str)

# printing result
print("Extracted number list : " + str(res))
