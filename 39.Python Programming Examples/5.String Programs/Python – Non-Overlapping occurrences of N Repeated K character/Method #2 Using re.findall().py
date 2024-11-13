# Python3 code to demonstrate working of
# Non-Overlapping occurrences of N Repeated K character
# Using re.findall()
import re

# initializing string
test_str = 'aaabaaaabbaa'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "a"

# initializing N
N = 2

# getting length using len()
# getting all occ. of substring
res = len(re.findall(K * N, test_str))

# printing result
print("The Non-Overlapping occurrences : " + str(res))
