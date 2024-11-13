# Python3 code to demonstrate working of
# Minimum element in tuple list
# using min() + map() + chain.from_iterable()
from itertools import chain

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Minimum element in tuple list
# using min() + map() + chain.from_iterable()
res = min(map(int, chain.from_iterable(test_list)))

# printing result
print("The Minimum element of list is : " + str(res))
