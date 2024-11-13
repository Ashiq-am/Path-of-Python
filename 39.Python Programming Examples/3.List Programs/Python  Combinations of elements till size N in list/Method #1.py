# Python3 code to demonstrate working of
# Combinations of elements till size N in list
# Using list comprehension + combinations()
from itertools import combinations

# initializing list
test_list = [4, 5, 6, 7, 3, 8]

# printing original list
print("The original list is : " + str(test_list))

# Combinations of elements till size N in list
# Using list comprehension + combinations()
res = [com for sub in range(3) for com in combinations(test_list, sub + 1)]

# Printing result
print("The combinations of elements till length N : " + str(res))
