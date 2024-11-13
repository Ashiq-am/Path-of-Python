# Python3 code to demonstrate working of
# Convert Nested List to 1 value Tuple
# Using isinstance() + recursion

# helper_fnc
def hlper_fnc(test_list):
	res = []
	if isinstance(test_list, list):
		for ele in test_list:
			res.extend(hlper_fnc(ele))
	elif isinstance(test_list, int):
		res.append((test_list, ))
	return res

# initializing list
test_list = [[5, [6]], [4, 7, [10, 45]], [12], [9, 11]]

# printing original list
print("The original list is : " + str(test_list))

# Convert Nested List to 1 value Tuple
# Using isinstance() + recursion
res = hlper_fnc(test_list)

# printing result
print("The converted container : " + str(res))
