# Python3 code to demonstrate working of
# Distinct Data Type Rows
# Using type() + list comprehension

# initializing list
test_list = [[4, 3, 1], ["gfg", 3, {4: 2}], [3, 1, "jkl"], [9, (2, 3)]]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:

	# get Distinct types size
	type_size = len(list(set([type(ele) for ele in sub])))

	# if equal get result
	if len(sub) == type_size:
		res.append(sub)

# printing result
print("The Distinct data type rows : " + str(res))
