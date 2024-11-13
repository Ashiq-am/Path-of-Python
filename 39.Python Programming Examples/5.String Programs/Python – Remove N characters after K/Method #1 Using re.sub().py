# Python3 code to demonstrate working of
# Remove N characters after K
# Using re.sub()
import re

# initializing strings
test_str = 'geeksfor@123geeks is best@212 for cs'

# printing original string
print("The original string is : " + str(test_str))

# initializing N
N = 3

# initializing K
K = '@'

# using re.sub() to perform task
res = re.sub(r'\@...', '', test_str)

# printing result
print("The String after removal : " + str(res))
