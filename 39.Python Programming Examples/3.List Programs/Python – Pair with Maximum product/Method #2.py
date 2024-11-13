# Python3 code to demonstrate
# Pair with Maximum product
# using list comprehension + nlargest() + combinations() + lambda
from itertools import combinations
from heapq import nlargest

# initializing list
test_list = [3, 4, 1, 7, 9, 8]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + nlargest() + combinations() + lambda
# Pair with Maximum product
# computes 2 max product pair
res = nlargest(2, combinations(test_list, 2), key = lambda sub: abs(sub[0] * sub[1]))

# print result
print("The maximum product pair is : " + str(res))
