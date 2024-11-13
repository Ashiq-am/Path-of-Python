# Python 3 code to demonstrate
# check if list are identical
# using map() + reduce()
import functools

# initializing lists
test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

# printing lists
print ("The first list is : " + str(test_list1))
print ("The second list is : " + str(test_list2))

# using map() + reduce() to check if
# lists are equal
if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, test_list1, test_list2), True) :
	print ("The lists are identical")
else :
	print ("The lists are not identical")
