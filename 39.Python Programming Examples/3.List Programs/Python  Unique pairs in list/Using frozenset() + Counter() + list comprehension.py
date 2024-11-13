# Python3 code to demonstrate working of
# Unique pairs in list
# using frozenset() + Counter() + list comprehension
from collections import Counter

# initialize list
test_list = [[5, 6], [9, 8], [8, 9], [1, 4], [6, 5], [10, 1]]

# printing original list
print("The original list is : " + str(test_list))

# Unique pairs in list
# using frozenset() + Counter() + list comprehension
temp = Counter(frozenset(ele) for ele in test_list)
res = [temp[frozenset(ele)] == 1 for ele in test_list]

# printing result
print("The Unique status of elements is " + str(res))
