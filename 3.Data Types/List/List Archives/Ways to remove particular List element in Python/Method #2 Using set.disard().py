# Python code to demonstrate
# element removal in list
# using discard() method

test_list1 = [1, 3, 4, 6, 3]
test_list2 = [1, 4, 5, 4, 5]

# Printing initial list
print ("The list before element removal is : "
							+ str(test_list2))

# using discard() to remove list element 4
test_list2 = set(test_list2)
test_list2.discard(4)

test_list2 = list(test_list2)

# Printing list after removal
# removes element as distinct initially
print ("The list after element removal is : "
						+ str(test_list2))
