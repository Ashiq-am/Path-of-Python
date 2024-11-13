# Python 3 code to demonstrate
# to remove elements present in other list
# using filter() + lambda

# initializing list
test_list = [1, 3, 4, 6, 7]

# initializing remove list
remove_list = [3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# printing remove list
print ("The original list is : " + str(remove_list))

# using filter() + lambda to perform task
res = filter(lambda i: i not in remove_list, test_list)

# printing result
print ("The list after performing remove operation is : " + str(res))
