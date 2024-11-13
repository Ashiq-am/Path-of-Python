# Python3 code to demonstrate working of
# Replace numbers by K in String
# Using regex() + sub()
import re

# initializing string
test_str = 'G4G is 4 all No. 1 Geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '@'

# using regex expression to solve problem
res = re.sub(r'\d', K, test_str)

# printing result
print("The resultant string : " + str(res))
