# Python3 code to demonstrate
# Removing element from list of lists
# using list comprehension + list slicing

# initializing list
test_list = [[4, 5, 6], [5, 6, 4, 1], [4], [4, 8, 9, 10]]

# printing original list
print("The original list : " + str(test_list))

# initializing Number to delete
N = 4

# using list comprehension + list slicing
# Removing element from list of lists
for sub in test_list:
	sub[:] = [ele for ele in sub if ele != N]

# print result
print("The list after deletion of element : " + str(test_list))
