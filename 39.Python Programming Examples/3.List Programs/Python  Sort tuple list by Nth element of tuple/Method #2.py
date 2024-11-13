# Python3 code to demonstrate working of
# Sort tuple list by Nth element of tuple
# using sort() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]

# printing original list
print("The original list is : " + str(test_list))

# index according to which sort to perform
N = 1

# Sort tuple list by Nth element of tuple
# using sort() + itemgetter()
test_list.sort(key = itemgetter(N))

# printing result
print("List after sorting tuple by Nth index sort : " + str(test_list))
