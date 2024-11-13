# Python3 code to demonstrate working of
# All replacement combination from other list
# Using combinations() + len()
from itertools import combinations

# initializing list
test_list = [4, 1, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing replacement list
repl_list = [8, 10]

# using combinations() to get all combinations replacements
res = list(combinations(test_list + repl_list, len(test_list)))

# printing result
print("All combinations replacements from other list : " + str(res))
