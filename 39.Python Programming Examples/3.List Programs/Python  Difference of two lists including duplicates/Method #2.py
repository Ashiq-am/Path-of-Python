# Python code to demonstrate
# Difference of list including duplicates
# Using map() + lambda + remove()

# initializing lists
test_list1 = [1, 3, 4, 5, 1, 3, 3]
test_list2 = [1, 3, 5]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Using map() + lambda + remove()
# Difference of list including duplicates
res = map(lambda x: test_list1.remove(x)
		if x in test_list1 else None, test_list2)

# print result
print("The list after performing the subtraction : " + str(test_list1))
