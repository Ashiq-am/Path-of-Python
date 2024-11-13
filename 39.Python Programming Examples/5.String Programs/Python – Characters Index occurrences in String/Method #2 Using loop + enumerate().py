# Python3 code to demonstrate working of
# Characters Index occurrences in String
# Using loop + enumerate()
import re

# initializing string
test_str = "Gfg is best for geeks"

# printing original string
print("The original string is : " + test_str)

# Characters Index occurrences in String
# Using loop + enumerate()
res = {ele : [] for ele in test_str}
for idx, ele in enumerate(test_str):
	res[ele].append(idx)

# printing result
print("Characters frequency index dictionary : " + str(res))
