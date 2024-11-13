# Python3 code to demonstrate working of
# Substitute character with its occurrence
# Using lambda + regex + next()
from itertools import count
import re

# initializing string
test_str = "geeksforgeeks is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing letter
test_let = 'g'

# Substitute character with its occurrence
# Using lambda + regex + next()
cnt = count(1)
res = re.sub(r"g", lambda x: "{}".format(next(cnt)), test_str)

# printing result
print("The string after performing substitution : " + str(res))
