# Python3 code to demonstrate working of
# Construct Sum pairs equal to K
# Using combinations() + sum()
from itertools import combinations

# initializing list
test_list = [3, 4, 0, 5, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# Construct Sum pairs equal to K
# Using combinations() + sum()
res = [ele for ele in combinations(test_list, 2) if sum(ele) == K]

# printing result
print("The paired tuples equal to K : " + str(res))
