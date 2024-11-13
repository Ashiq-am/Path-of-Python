# Python3 code to demonstrate working of
# Farthest point on horizontal lines in 2D plane
# Using list comprehension + max()
from collections import defaultdict

# initializing list
test_list = [(1, 6), (4, 6), (2, 6), (6, 8), (1, 8), (2, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Using list comprehension + max()
# Farthest point on horizontal lines in 2D plane
temp = defaultdict(list)
for key, val in test_list:
    temp[val].append(key)
res = [(key, val) for key, val in test_list if max(temp[val]) == key]

# Printing result
print("The list after filtering just maximum points on lines : " + str(res))
