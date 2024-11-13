# Python3 code to demonstrate working of
# Remove Consecutive tuple according to key
# using itemgetter() + next() + groupby()
from operator import itemgetter
from itertools import groupby

# initialize list
test_list = [(4, 5), (4, 6), (7, 8), (7, 1), (7, 0), (8, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Remove Consecutive tuple according to key
# using itemgetter() + next() + groupby()
res = [next(group) for key, group in groupby(test_list, key = itemgetter(0))]

# printing result
print("List after Consecutive tuple removal : " + str(res))
