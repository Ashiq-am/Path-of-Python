# Python3 code to demonstrate working of
# Group Tuples by Kth Index Element
# Using groupby() + itemegetter() + generator expression
from operator import itemgetter
from itertools import groupby

# initializing lists
test_list = [(4, 5), (3, 2), (2, 2), (1, 2), (5, 5)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# Group Tuples by Kth Index Element
# Using groupby() + itemegetter() + generator expression
test_list.sort()
res = list(tuple(sub) for idx, sub in groupby(test_list, key = itemgetter(K)))

# printing result
print("Tuples after grouping : " + str(res))
