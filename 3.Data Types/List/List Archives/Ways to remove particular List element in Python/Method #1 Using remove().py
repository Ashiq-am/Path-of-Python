# Python code to demonstrate
# element removal in list
# using remove() method

test_list1 = [1, 3, 4, 6, 3]
test_list2 = [1, 4, 5, 4, 5]

# Printing initial list
print ("The list before element removal is : "
							+ str(test_list1))

# using remove() to remove list element3
test_list1.remove(3)

# Printing list after removal
# only first occurrence deleted
print ("The list after element removal is : "
						+ str(test_list1))
