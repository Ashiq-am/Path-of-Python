# Python3 code to demonstrate working of
# Sort Dictionaries by Size
# Using len() + sort()

# function to get length
def get_len(sub):

	# return length
	return len(sub)


# initializing list
test_list = [{4: 6, 9: 1, 10: 2, 2: 8}, {
	4: 3, 9: 1}, {3: 9}, {1: 2, 9: 3, 7: 4}]

# printing original lists
print("The original list is : " + str(test_list))

# performing inplace sort of list
test_list.sort(key=get_len)

# printing result
print("Sorted List : " + str(test_list))
