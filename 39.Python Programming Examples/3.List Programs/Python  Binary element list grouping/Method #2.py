# Python3 code to demonstrate
# to perform binary list grouping
# using itertools.groupby() + itemgetter()
from itertools import groupby
from operator import itemgetter

# initializing list
test_list = [["G", 0], ["F", 0], ["B", 2],
			["E", 2], ['I', 1], ['S', 1],
			['S', 2], ['T', 2], ['G', 0]]

# using itertools.groupby() + itemgetter()
# to perform binary list grouping
test_list.sort(key = itemgetter(1))
groups = groupby(test_list, itemgetter(1))
res = [[i[0] for i in val] for (key, val) in groups]

# printing result
print ("The grouped list is : " + str(res))
