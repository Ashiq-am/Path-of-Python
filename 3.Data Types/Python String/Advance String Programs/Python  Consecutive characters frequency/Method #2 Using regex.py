# Python3 code to demonstrate working of
# Consecutive characters frequency
# Using regex
import re

# initializing string
test_str = "geekksforgggeeks"

# printing original string
print("The original string is : " + test_str)

# Consecutive characters frequency
# Using regex
res = [len(sub.group()) for sub in re.finditer(r'(.)\1*', test_str)]

# printing result
print("The Consecutive characters frequency : " + str(res))
