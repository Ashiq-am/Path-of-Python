# Python3 code to demonstrate working of
# Cummulative Records Product
# using product + map() + chain.from_iterable()
from itertools import chain

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Cummulative Records Product
# using product + map() + chain.from_iterable()
res = prod(map(int, chain.from_iterable(test_list)))

# printing result
print("The cummulative product of list is : " + str(res))
