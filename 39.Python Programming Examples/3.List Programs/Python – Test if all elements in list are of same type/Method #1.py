# Python3 code to demonstrate
# Test if all elements in list are of same type
# using loop + isinstance()

# Initializing lists
test_list = [5, 6, 2, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# Test if all elements in list are of same type
# using loop + isinstance()
res = True
for ele in test_list:
	if not isinstance(ele, type(test_list[0])):
		res = False
		break

# printing result
print ("Do all elements have same type : " + str(res))
