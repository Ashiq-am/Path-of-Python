# Python3 code to demonstrate
# Maximum Aggretation Pair in List
# using list comprehension + max() + combinations() + lambda
from itertools import combinations

# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + max() + combinations() + lambda
# Maximum Aggretation Pair in List
res = max(combinations(test_list, 2), key = lambda sub: sub[0] + sub[1])

# print result
print("The maximum sum pair is : " + str(res))
