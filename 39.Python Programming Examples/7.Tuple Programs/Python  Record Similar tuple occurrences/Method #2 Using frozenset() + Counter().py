# Python3 code to demonstrate working of
# Record Similar tuple occurrences
# Using frozenset() + Counter()
from collections import Counter

# initialize list
test_list = [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]

# printing original list
print("The original list is : " + str(test_list))

# Record Similar tuple occurrences
# Using frozenset() + Counter()
res = dict(Counter(tuple(frozenset(ele)) for ele in test_list))

# printing result
print("The frequency of like tuples : " + str(res))
