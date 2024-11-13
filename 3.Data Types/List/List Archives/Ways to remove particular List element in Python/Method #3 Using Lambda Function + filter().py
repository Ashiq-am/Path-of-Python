# Python code to demonstrate
# element removal in list
# using filter() + Lambda function

test_list1 = [1, 3, 4, 6, 3]
test_list2 = [1, 4, 5, 4, 5]

# Printing initial list
print ("The list before element removal is : "
							+ str(test_list1))

# using filter() + Lambda function
# to remove list element 3
test_list1 = list(filter(lambda x: x != 3, test_list1))

# Printing list after removal
print ("The list after element removal is : "
						+ str(test_list1))
