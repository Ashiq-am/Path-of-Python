# Python3 code to demonstrate working of
# Shift sublist in list
# Using list slicing

# function to perform the task
def shift_sublist(test_list, strt_idx, no_ele, shft_idx):
	return (test_list[:strt_idx] + test_list[strt_idx + no_ele : no_ele + shft_idx - 1]
			+ test_list[strt_idx : strt_idx + no_ele] + test_list[shft_idx + no_ele -1:])

# initializing list
test_list = [4, 5, 6, 7, 3, 8, 10, 1, 12, 15, 16]

# printing original list
print("The original list is : " + str(test_list))

# Using list slicing
# Shift sublist in list
res = shift_sublist(test_list, 2, 3, 6)

# Printing result
print("The list after shift of sublist : " + str(res))
