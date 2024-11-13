# Python 3 code to demonstrate
# to remove elements present in other list
# using set()

# initializing list
test_list = [1, 3, 4, 6, 7]

# initializing remove list
remove_list = [3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# printing remove list
print ("The original list is : " + str(remove_list))

# using set() to perform task
set1 = set(test_list)
set2 = set(remove_list)
res = list(set1 - set2)

# printing result
print ("The list after performing remove operation is : " + str(res))
