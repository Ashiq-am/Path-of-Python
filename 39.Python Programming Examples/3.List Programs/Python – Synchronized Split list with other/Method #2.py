# Python3 code to demonstrate working of
# Synchronized Split list with other
# Using chain.from_iterables() + zip()
from itertools import chain

# initializing list
test_list = [5, 6, 3, 7, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing String list
str_list = ['Gfg', 'is best', 'I love', 'Gfg', 'and CS']

# Synchronized Split list with other
# Using chain.from_iterables() + zip()
res = list(chain.from_iterable([[sub1] * len(sub2.split()) for sub1, sub2 in zip(test_list, str_list)]))

# printing result
print("Mapped list elements : " + str(res))
