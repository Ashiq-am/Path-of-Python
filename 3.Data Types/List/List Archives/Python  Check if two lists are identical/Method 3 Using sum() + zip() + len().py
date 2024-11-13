# Python 3 code to demonstrate
# check if list are identical
# using sum() + zip() + len()

# initializing lists
test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

# printing lists
print ("The first list is : " + str(test_list1))
print ("The second list is : " + str(test_list2))

# using sum() + zip() + len() to check if
# lists are equal
if len(test_list1)== len(test_list2) and len(test_list1) == sum([1 for i, j in zip(test_list1, test_list2) if i == j]):
	print ("The lists are identical")
else :
	print ("The lists are not identical")
