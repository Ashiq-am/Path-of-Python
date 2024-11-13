# Python3 code to demonstrate
# maximum difference pair
# using list comprehension + nlargest() + combinations() + lambda
from itertools import combinations
from heapq import nlargest

# initializing list
test_list = [3, 4, 1, 7, 9, 8]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + max() + combinations() + lambda
# maximum difference pair
# computes 2 maximum pair differences
res = nlargest(2, combinations(test_list, 2),
		key = lambda sub: abs(sub[0]-sub[1]))

# print result
print("The maximum difference pair is : " + str(res))
