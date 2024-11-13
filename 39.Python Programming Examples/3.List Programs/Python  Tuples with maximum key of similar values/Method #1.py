# Python3 code to demonstrate working of
# Tuples with maximum key of similar values
# using max() + groupby() + itemgetter() + list comprehension
from operator import itemgetter
from itertools import groupby

# initialize list
test_list = [(4, 3), (2, 3), (3, 10), (5, 10), (5, 6)]

# printing original list
print("The original list : " + str(test_list))

# Tuples with maximum key of similar values
# using max() + groupby() + itemgetter() + list comprehension
res = [max(values) for key, values in groupby(test_list, key = itemgetter(1))]

# printing result
print("The records retaining maximum keys of similar values : " + str(res))
