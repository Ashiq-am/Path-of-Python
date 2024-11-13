# Python code to demonstrate
# Remove Front K elements
# using len() + list slicing

# initializing list
test_list = [1, 4, 6, 3, 5, 8]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using len() + list slicing
# Remove Front K elements
res = test_list[K:]

# printing result
print ("The list after removing first K elements : " + str(res))
