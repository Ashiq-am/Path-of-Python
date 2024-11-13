# Python3 code to demonstrate working of
# Merge key value list
# Using itemgetter() + groupby() + zip()
from itertools import groupby
from operator import itemgetter

# initializing lists
test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]
test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']

# printing original lists
print("The original list1 is : " + str(test_list1))
print("The original list2 is : " + str(test_list2))

# Using itemgetter() + groupby() + zip()
# Merge key value list
res = {keys: [i for _, i in sub] for keys, sub in groupby(zip(test_list1, test_list2), key = itemgetter(0))}

# printing result
print("The merged key value dictionary is : " + str(dict(res)))
