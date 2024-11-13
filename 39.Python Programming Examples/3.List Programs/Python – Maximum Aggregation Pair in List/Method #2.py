# Python3 code to demonstrate
# Maximum Aggretation Pair in List
# using list comprehension + nlargest() + combinations() + lambda
from itertools import combinations
from heapq import nlargest

# initializing list
test_list = [3, 4, 1, 7, 9, 8]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + nsmallest() + combinations() + lambda
# Maximum Aggretation Pair in List
# computes 2 max sum pair
res = nlargest(2, combinations(test_list, 2), key = lambda sub: sub[0] + sub[1])

# print result
print("The maximum sum pair is : " + str(res))
