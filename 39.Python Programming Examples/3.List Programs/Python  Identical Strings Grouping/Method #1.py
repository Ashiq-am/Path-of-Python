# Python3 code to demonstrate
# Identical Strings Grouping
# using collections.Counter()
import collections

# initializing list
test_list = ["Gfg", "best", "is", "Gfg", "is", "best", "Gfg", "best"]

# printing original list
print("The original list : " + str(test_list))

# using collections.Counter()
# Identical Strings Grouping
temp = collections.Counter(test_list)
res = [[i] * j for i, j in temp.items()]

# print result
print("The Strings after grouping are : " + str(res))
