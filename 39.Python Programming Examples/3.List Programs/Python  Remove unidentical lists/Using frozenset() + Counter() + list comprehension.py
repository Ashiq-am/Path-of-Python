# Python3 code to demonstrate working of
# Remove unidentical lists
# using frozenset() + Counter() + list comprehension
from collections import Counter

# initialize list
test_list = [[5, 6], [9, 8], [8, 9], [1, 4], [6, 5], [10, 1]]

# printing original list
print("The original list is : " + str(test_list))

# Remove unidentical lists
# using frozenset() + Counter() + list comprehension
temp = Counter(frozenset(ele) for ele in test_list)
res = [ele for ele in test_list if temp[frozenset(ele)] >= 2]

# printing result
print("The list after removal of unidentical lists : " + str(res))
