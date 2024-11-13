# Python3 code to demonstrate working of
# Segregate Positive and Negative Integers
# Using regex
import re

# initializing string
test_str = "gfg + 4-1is + 5best-8"

# printing original string
print("The original string is : " + test_str)

# Segregate Positive and Negative Integers
# Using regex
res = re.findall('[-+]?\d+', test_str)

# printing result
print("The split string is : " + str(res))
