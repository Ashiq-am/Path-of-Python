# Python code to demonstrate
# to sort according to other list
# using sort() + lambda + index()

# initializing list of tuples
test_list = [ ('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# initializing sort order
sort_order = ['d', 'c', 'a', 'b']

# printing original list
print ("The original list is : " + str(test_list))

# printing sort order list
print ("The sort order list is : " + str(sort_order))

# using sort() + lambda + index()
# to sort according to other list
# test_list.sort(key = lambda(i, j): sort_order.index(i)) # works in python 2
test_list.sort(key = lambda i: sort_order.index(i[0])) # works in python 3

# printing result
print ("The sorted list is : " + str(test_list))
