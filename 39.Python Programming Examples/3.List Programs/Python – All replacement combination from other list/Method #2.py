# Python3 code to demonstrate working of
# All replacement combination from other list
# Using combinations() + extend()
from itertools import combinations

# initializing list
test_list = [4, 1, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing replacement list
repl_list = [8, 10]

# using combinations() to get all combinations replacements
# extend() for concatenation
n = len(test_list)
test_list.extend(repl_list)
res = list(combinations(test_list, n))

# printing result
print("All combinations replacements from other list : " + str(res))
