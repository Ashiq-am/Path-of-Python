# Python3 code to demonstrate working of
# Convert list of tuples to dictionary value lists
# Using defaultdict() + groupby()
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

# initializing list
test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]

# printing original list
print("The original list is : " + str(test_list))

# Using defaultdict() + groupby()
# Convert list of tuples to dictionary value lists
res = dict((k, [v[1] for v in itr]) for k, itr in groupby(
								test_list, itemgetter(0)))

# printing result
print("The merged dictionary is : " + str(dict(res)))
