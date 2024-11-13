# Python3 code to demonstrate working of
# Maximum of Similar Keys in Tuples
# Using max() + groupby() + itemgetter() + list comprehension
from itertools import groupby
from operator import itemgetter

# initializing lists
test_list = [(4, 8), (3, 2), (2, 2), (4, 6), (3, 7), (4, 5)]

# printing original list
print("The original list is : " + str(test_list))

# Maximum of Similar Keys in Tuples
# Using max() + groupby() + itemgetter() + list comprehension
temp = groupby(sorted(test_list, key = itemgetter(0)), key = itemgetter(0))
res = [(key, max(map(itemgetter(1), sub))) for key, sub in temp]

# printing result
print("Maximum grouped elements : " + str(res))
