# Python3 code to demonstrate working of
# Size Range Combinations in list
# Using list comprehension + combinations()
from itertools import combinations

# initializing list
test_list = [4, 5, 6, 7, 3, 8]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 2, 4

# Size Range Combinations in list
# Using list comprehension + combinations()
res1 = [com for sub in range(j) for com in combinations(test_list, sub + 1)]
res2 = [com for sub in range(i - 1) for com in combinations(test_list, sub + 1)]
res = list(set(res1) - set(res2))

# Printing result
print("The combinations of elements in range of i and j : " + str(res))
