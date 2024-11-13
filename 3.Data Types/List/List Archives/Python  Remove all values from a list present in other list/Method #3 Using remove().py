# Python 3 code to demonstrate
# to remove elements present in other list
# using remove()

# initializing list
test_list = [1, 3, 4, 6, 7]

# initializing remove list
remove_list = [3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# printing remove list
print ("The original list is : " + str(remove_list))

# using remove() to perform task
# handled exceptions.
for i in remove_list:
	try:
		test_list.remove(i)
	except ValueError:
		pass

# printing result
print ("The list after performing remove operation is : " + str(test_list))
