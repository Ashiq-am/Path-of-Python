# sorting util.
def get_count(sub):
	return len([ele for ele in sub if ele in cus_list])


# initializing list
test_list = [[4, 5, 1, 7], [6, 5], [9, 8, 2], [7, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing custom list
cus_list = [4, 5, 7]

# performing inplace sort
test_list.sort(key=get_count)

# printing result
print("Sorted Matrix : " + str(test_list))
