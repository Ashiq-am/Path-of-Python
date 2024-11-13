# Python3 code to demonstrate working of
# Group contiguous strings in List
# Using isinstance() + generator + groupby()
from itertools import groupby

# checking string instance
def str_check(ele):
	return isinstance(ele, str)


def group_strs(test_list):

	# grouping list by cont. strings
	for key, grp in groupby(test_list, key=str_check):
		if key:
			yield list(grp)
		else:
			yield from grp


# initializing list
test_list = [5, 6, 'g', 'f', 'g', 6, 5,
			'i', 's', 8, 'be', 'st', 9]

# printing original list
print("The original list is : " + str(test_list))

# calling recursion fnc.
res = [*group_strs(test_list)]

# printing result
print("List after grouping : " + str(res))
