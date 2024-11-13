# Python code to demonstrate
# ways to iterate tuples list of list into single list
# using itertools.ziplongest + lambda + chain

# import library
from itertools import zip_longest, chain

# initialising listoflist
test_list = [
		[('11'), ('12'), ('13')],
		[('21'), ('22'), ('23')],
		[('31'), ('32'), ('33')]
		]


# printing intial list
print ("Initial List = ", test_list)

# iterate list tuples list of list into single list
# using lambda + chain + filter
res_list = list(filter(lambda x: x, chain(*zip_longest(*test_list))))

# print final List
print ("Resultant List = ", res_list)
