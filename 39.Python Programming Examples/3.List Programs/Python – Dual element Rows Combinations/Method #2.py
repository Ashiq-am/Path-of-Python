# Python3 code to demonstrate
# Dual element Rows Combinations
# using map() + lambda + combinations()
from itertools import combinations

# Initializing list
test_list = [[3, 4], [5, 6], [7, 8]]

# printing original list
print("The original list is : " + str(test_list))

# Dual element Rows Combinations
# using map() + lambda + combinations()
res = list(map(lambda ele: ele[0] + ele[1], combinations(test_list, 2)))

# printing result
print ("Combination of dual rows list is : " + str(res))
