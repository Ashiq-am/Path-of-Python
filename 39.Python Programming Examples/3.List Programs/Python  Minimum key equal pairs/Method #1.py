# Python3 code to demonstrate working of
# Minimum key equal pairs
# using min() + groupby() + itemgetter() + list comprehension
from operator import itemgetter
from itertools import groupby

# initialize list
test_list = [(4, 3), (2, 3), (3, 10), (5, 10), (5, 6)]

# printing original list
print("The original list : " + str(test_list))

# Minimum key equal pairs
# using min() + groupby() + itemgetter() + list comprehension
res = [min(values) for key, values in groupby(test_list, key = itemgetter(1))]

# printing result
print("Minimum key equal pairs : " + str(res))
