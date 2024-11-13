# Python3 code to demonstrate working of
# Longest Substring of K
# Using findall() + max()
import re

# initializing string
test_str = 'abcaaaacbbaa'

# printing original String
print("The original string is : " + str(test_str))

# initializing K
K = 'a'

# getting all substrings
res = re.findall(r'' + K + '+', test_str)

# getting maximum of substrings Length
res = len(max(res, key = len))

# printing result
print("The Longest Substring Length : " + str(res))
