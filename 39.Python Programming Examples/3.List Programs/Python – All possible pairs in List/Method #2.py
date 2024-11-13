# Python3 code to demonstrate working of
# All possible pairs in List
# Using combinations()
from itertools import combinations

# initializing list
test_list = [1, 7, 4, 3]

# printing original list
print("The original list : " + str(test_list))

# All possible pairs in List
# Using combinations()
res = list(combinations(test_list, 2))

# printing result
print("All possible pairs : " + str(res))
