# Python3 code to demonstrate
# Check for None value in Matrix
# using set.issubset() + itertools.chain()
from itertools import chain

# initializing list
test_list = [[4, 5, 6],
			[10, 2, None],
			[1, 11, 18]]

# printing original list
print("The original list : " + str(test_list))

# using set.issubset() + itertools.chain()
# to Search in Matrix
res = {None}.issubset(chain.from_iterable(test_list))

# printing result
print("Does Matrix contain None value ? : " + str(res))
