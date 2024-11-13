# Python code to demonstrate
# element removal in list
# using pop() method

test_list1 = [1, 3, 4, 6, 3]

# Printing initial list
print ("The list before element removal is : "
							+ str(test_list1))

rmv_element = 4

# using pop()
# to remove list element 4
if rmv_element in test_list1:
	test_list1.pop(test_list1.index(rmv_element))

# Printing list after removal
print ("The list after element removal is : "+ str(test_list1))

