# Python3 code to demonstrate working of
# Overlapping Prefix - Suffix in Two Lists
# Using loop + slicing + startswith()
import re

# initializing strings
test_str1 = "Gfgisbest"
test_str2 = "bestforall"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

res = ''
for char in range(len(test_str1)):

    # using startswith() to get prefix
    if test_str2.startswith(test_str1[char:]):
        res = test_str1[char:]
        break

# printing result
print("Overlapped String : " + str(res))
