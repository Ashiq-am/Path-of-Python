# Python3 code to demonstrate
# sort list of tuples according to second
# using list comprehension + filter() + lambda

# initializing list of tuples
test_list = [('a', 2), ('c', 3), ('d', 4)]

# initializing sort order
sort_order = [4, 2, 3]

# printing the original list
print ("The original list is : " + str(test_list))

# printing sort order list
print ("The sort order list is : " + str(sort_order))

# using list comprehension + filter() + lambda
# sort list of tuples according to second
res = [i for j in sort_order
	for i in filter(lambda k: k[1] == j, test_list)]

# printing result
print ("The list after appropriate sorting : " + str(res))
