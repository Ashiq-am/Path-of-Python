# Python3 code to demonstrate working of
# Reorder for consecutive elements
# Using Counter() + elements()
from collections import Counter

# initializing list
test_list = [4, 7, 5, 4, 1, 4, 1, 6, 7, 5]

# printing original lists
print("The original list is : " + str(test_list))

# reordering using elements()
res = list(Counter(test_list).elements())

# printing result
print("Reordered List : " + str(res))
