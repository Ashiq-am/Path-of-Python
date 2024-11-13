# Python3 code to demonstrate working of
# Group Records on Similar index elements
# Using groupby() + generator expression
from itertools import groupby

# initializing list
test_list = [(4, 7, 13), (4, 5, 7), (6, 7, 10), (4, 5, 15), (6, 7, 12)]

# printing original list
print("The original list is : " + str(test_list))

# Group Records on Similar index elements
# Using groupby() + generator expression
test_list.sort()
res = tuple((*key, [tup[-1] for tup in val]) for key, val in groupby(test_list, lambda tup: tup[:2]))

# printing result
print("Tuples after grouping : " + str(res))
