# Python3 code to demonstrate working of
# Split by repeating substring
# Using re.findall()
import re

# initializing string
test_str = "gfggfggfggfggfggfggfggfg"

# printing original string
print("The original string is : " + test_str)

# initializing target
K = 'gfg'

# Split by repeating substring
# Using re.findall()
res = re.findall(K, test_str)

# printing result
print("The split string is : " + str(res))
