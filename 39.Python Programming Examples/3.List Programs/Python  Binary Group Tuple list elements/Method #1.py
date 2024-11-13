# Python3 code to demonstrate working of
# Binary Group Tuple list elements
# using generator + loop + zip()

# helper function to perform task
def bin_group(test_list):
	for tup1, tup2 in zip(test_list[0::2], test_list[1::2]):
			yield (tup1[0], tup1[1], tup2[1])

# initialize list
test_list = [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]

# printing original list
print("The original list : " + str(test_list))

# Binary Group Tuple list elements
# using generator + loop + zip()
res = list(bin_group(test_list))

# printing result
print("The list after binary grouping : " + str(res))
