# Python3 code to demonstrate working of
# Remove Kth Index Duplicates in Tuple
# Using groupby() + itemgetter() + list comprehension
from itertools import groupby
from operator import itemgetter

# initializing lists
test_list = [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4), (1, 2, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Remove Kth Index Duplicates in Tuple
# Using groupby() + itemgetter() + list comprehension
res = res = [list(val)[0] for key, val in groupby(sorted(test_list,
                                                         key=itemgetter(K)), key=itemgetter(K))]

# printing result
print("Filtered Tuples : " + str(res))
