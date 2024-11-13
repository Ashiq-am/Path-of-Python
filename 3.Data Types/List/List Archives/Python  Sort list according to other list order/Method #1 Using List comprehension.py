# Python3 code to demonstrate
# to sort according to other list
# using list comprehension

# initializing list of tuples
test_list = [ ('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# initializing sort order
sort_order = ['d', 'c', 'a', 'b']

# printing original list
print ("The original list is : " + str(test_list))

# printing sort order list
print ("The sort order list is : " + str(sort_order))

# using list comprehension
# to sort according to other list
res = [tuple for x in sort_order for tuple in test_list if tuple[0] == x]

# printing result
print ("The sorted list is : " + str(res))
