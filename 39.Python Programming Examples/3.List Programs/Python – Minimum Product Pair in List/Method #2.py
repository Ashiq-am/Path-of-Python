# Python3 code to demonstrate
# Minimum Product Pair in List
# using list comprehension + nsmallest() + combinations() + lambda
from itertools import combinations
from heapq import nsmallest

# initializing list
test_list = [3, 4, 1, 7, 9, 8]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + nsmallest() + combinations() + lambda
# Minimum Product Pair in List
res = nsmallest(2, combinations(test_list, 2), key = lambda sub: sub[0] * sub[1])

# print result
print("The minimum product pair is : " + str(res))
