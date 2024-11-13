# Python3 code to demonstrate working of
# Group tuple into list based on value
# using itemgetter() + list comprehension + groupby()
from operator import itemgetter
from itertools import groupby

# initialize list
test_list = [(1, 4), (2, 4), (6, 7), (5, 1), (6, 1), (8, 1)]

# printing original list
print("The original list : " + str(test_list))

# Group tuple into list based on value
# using itemgetter() + list comprehension + groupby()
res = [[i for i, j in temp]\
	for key, temp in groupby(test_list, key = itemgetter(1))]

# printing result
print("The list after grouping by value : " + str(res))
