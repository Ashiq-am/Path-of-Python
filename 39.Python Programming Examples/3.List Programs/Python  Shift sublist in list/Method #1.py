# Python3 code to demonstrate working of
# Shift sublist in list
# Using insert() + pop() + loop

# function to perform the task
def shift_sublist(test_list, strt_idx, no_ele, shft_idx):
	for ele in range(no_ele):
		test_list.insert(shft_idx + 1, test_list.pop(strt_idx))
	return test_list

# initializing list
test_list = [4, 5, 6, 7, 3, 8, 10, 1, 12, 15, 16]

# printing original list
print("The original list is : " + str(test_list))

# Using insert() + pop() + loop
# Shift sublist in list
res = shift_sublist(test_list, 2, 3, 6)

# Printing result
print("The list after shift of sublist : " + str(res))
