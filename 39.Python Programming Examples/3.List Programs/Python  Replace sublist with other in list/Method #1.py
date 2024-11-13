# Python3 code to demonstrate working of
# Replace sublist with other in list
# Using loop (when sublist is given)

# helper function to find elements
def find_sub_idx(test_list, repl_list, start = 0):
	length = len(repl_list)
	for idx in range(start, len(test_list)):
		if test_list[idx : idx + length] == repl_list:
			return idx, idx + length

# helper function to perform final task
def replace_sub(test_list, repl_list, new_list):
	length = len(new_list)
	idx = 0
	for start, end in iter(lambda: find_sub_idx(test_list, repl_list, idx), None):
		test_list[start : end] = new_list
		idx = start + length

# initializing list
test_list = [4, 5, 6, 7, 10, 2]

# printing original list
print("The original list is : " + str(test_list))

# Replace list
repl_list = [5, 6, 7]
new_list = [11, 1]

# Replace sublist with other in list
# Using loop (when sublist is given)
replace_sub(test_list, repl_list, new_list)

# printing result
print("List after replacing sublist : " + str(test_list))
