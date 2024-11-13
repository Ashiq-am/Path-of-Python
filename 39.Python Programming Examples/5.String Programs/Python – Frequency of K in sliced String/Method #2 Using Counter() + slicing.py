# Python3 code to demonstrate working of
# Frequency of K in sliced String
# Using Counter() + slicing
from collections import Counter

# initializing strings
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing i, j
i, j = 3, 20

# initializing K
K = 'e'

# slicing String
slc = test_str[i : j]

# Counter() is used to get count
res = Counter(slc)[K]

# printing result
print("The required Frequency : " + str(res))
