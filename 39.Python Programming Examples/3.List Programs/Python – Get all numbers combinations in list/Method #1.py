# Python3 code to demonstrate working of
# All numbers combinations
# Using list comprehension + combinations
from itertools import combinations

# initializing list
test_list = [59, 236, 31, 38, 23]

# printing original list
print("The original list : " + str(test_list))

# All numbers combinations
# Using list comprehension + combinations
res = [int(f"{x}{y}") for x, y in combinations(test_list, 2)]

# printing result
print("All numbers combinations : " + str(res))
