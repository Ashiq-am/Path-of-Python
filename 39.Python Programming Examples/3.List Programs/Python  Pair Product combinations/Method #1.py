# Python3 code to demonstrate working of
# Pair Product combinations
# Using list comprehension + combinations
from itertools import combinations

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# printing original list
print("The original list : " + str(test_list))

# Pair Product combinations
# Using list comprehension + combinations
res = [(b1 * a1, b2 * a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]

# printing result
print("The Product pair combinations are : " + str(res))
