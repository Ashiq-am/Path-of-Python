# Python3 code to demonstrate
# Pairing and combining nested list to tuple list
# using zip() + itertools.chain.from_iterable()
from itertools import chain

# initializing lists
test_list1 = [[1, 4, 5], [8, 7], [2]]
test_list2 = [['g', 'f', 'g'], ['f', 'r'], ['u']]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() + itertools.chain.from_iterable()
# Pairing and combining nested list to tuple list
res = list(zip(chain.from_iterable(test_list1),
			chain.from_iterable(test_list2)))

# print result
print("The paired list of tuple is : " + str(res))
