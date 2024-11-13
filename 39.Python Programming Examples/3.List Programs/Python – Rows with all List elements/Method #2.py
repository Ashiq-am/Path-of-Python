# Python3 code to demonstrate working of
# Rows with all List elements
# Using all() + list comprehension

# initializing list
test_list = [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing list
sub_list = [1, 2]

# testing elements presence using all()
res = [row for row in test_list if all(ele in row for ele in sub_list)]

# printing result
print("Rows with list elements : " + str(res))
