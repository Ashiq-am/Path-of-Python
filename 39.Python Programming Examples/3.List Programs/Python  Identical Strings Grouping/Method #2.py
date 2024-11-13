# Python3 code to demonstrate
# Identical Strings Grouping
# using itertools.groupby()
import itertools

# initializing list
test_list = ["Gfg", "best", "is", "Gfg", "is", "best", "Gfg", "best"]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby()
# Identical Strings Grouping
res = [list(i) for j, i in itertools.groupby(sorted(test_list))]

# print result
print("The Strings after grouping are : " + str(res))
