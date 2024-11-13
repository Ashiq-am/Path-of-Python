# Python code to demonstrate working of
# Group elements on break positions in list
# using itemgetter() + map() + lambda() + groupby()
from itertools import groupby
from operator import itemgetter

# initialize list
test_list = [1, 2, 4, 5, 6, 8, 9, 11]

# printing original list
print("The original list is : " + str(test_list))

# Group elements on break positions in list
# using itemgetter() + map() + lambda() + groupby()
res = list(map(itemgetter(1), j) for i, j in
		groupby(enumerate(test_list), lambda x, y : x - y))

# printing result
print("Grouping of elements at breaks : " + str(res))
