# Python3 code to demonstrate working of
# Consecutive element swapping in String
# using regular expression
import re

# initializing string
test_str = "gfgisbesty"

# printing original string
print("The original string is : " + test_str)

# Consecutive element swapping in String
# using regular expression
res = re.sub(r'(.)(.)', r'\2\1', test_str)

# printing result
print("String after Consecutive Swapping : " + str(res))
