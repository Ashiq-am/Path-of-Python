# Python3 code to demonstrate working of
# Longest Run of Character in String
# Using max() + re.findall()
import re

# initializing string
test_str = 'geeksforgeeeks'

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 'e'

# Longest Run of Character in String
# Using max() + re.findall()
res = len(max(re.findall(K + '+', test_str), key = len))

# printing result
print("Longest Run length of K : " + str(res))
