# Python3 code to demonstrate
# sort list of tuples according to second
# using sorted() + index() + lambda

# initializing list of tuples
test_list = [('a', 2), ('c', 3), ('d', 4)]

# initializing sort order
sort_order = [4, 2, 3]

# printing the original list
print ("The original list is : " + str(test_list))

# printing sort order list
print ("The sort order list is : " + str(sort_order))

# using sorted() + index() + lambda
# sort list of tuples according to second
res = list(sorted(test_list,
	key = lambda i: sort_order.index(i[1])))

# printing result
print ("The list after appropriate sorting : " + str(res))
