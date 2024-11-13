# Python3 code to demonstrate working of
# Record Similar tuple occurrences
# Using Counter() + map() + sorted
from collections import Counter

# initialize list
test_list = [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]

# printing original list
print("The original list is : " + str(test_list))

# Record Similar tuple occurrences
# Using Counter() + map() + sorted
res = dict(Counter(tuple(ele) for ele in map(sorted, test_list)))

# printing result
print("The frequency of like tuples : " + str(res))
