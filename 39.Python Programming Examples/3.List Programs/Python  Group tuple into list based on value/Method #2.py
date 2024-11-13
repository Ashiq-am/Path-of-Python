# Python3 code to demonstrate working of
# Group tuple into list based on value
# using map() + itemgetter() + groupby() + list comprehension
from operator import itemgetter
from itertools import groupby

# initialize list
test_list = [(1, 4), (2, 4), (6, 7), (5, 1), (6, 1), (8, 1)]

# printing original list
print("The original list : " + str(test_list))

# Group tuple into list based on value
# using map() + itemgetter() + groupby() + list comprehension
res = [list(map(itemgetter(0), temp))
	for (key, temp) in groupby(test_list, itemgetter(1))]

# printing result
print("The list after grouping by value : " + str(res))
