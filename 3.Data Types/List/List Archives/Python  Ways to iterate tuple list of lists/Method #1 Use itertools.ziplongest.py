# Python code to demonstrate ways to iterate
# tuples list of list into single list
# using itertools.ziplongest

# import library
from itertools import zip_longest

# initialising listoflist
test_list = [
		[('11'), ('12'), ('13')],
		[('21'), ('22'), ('23')],
		[('31'), ('32'), ('33')]
		]


# printing intial list
print ("Initial List = ", test_list)

# iterate list tuples list of list into single list
res_list = [item for my_list in zip_longest(*test_list)
						for item in my_list if item]

# print final List
print ("Resultant List = ", res_list)
