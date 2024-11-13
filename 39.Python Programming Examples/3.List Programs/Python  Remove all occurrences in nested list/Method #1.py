# Python3 code to demonstrate
# Remove all occurrences in nested list
# using list comprehension

# initializing list
test_list = [[4, 5], [1, 2, 3], [4, 5], [8, 9], [10, 11]]

# initializing list to delete
del_list = [4, 5]

# printing original list
print("The original list : " + str(test_list))

# printing delete list
print("The list to be deleted is : " + str(del_list))

# using list comprehension
# Remove all occurrences in nested list
res = [i for i in test_list if i != del_list]

# print result
print("The list after removal of list element : " + str(res))
