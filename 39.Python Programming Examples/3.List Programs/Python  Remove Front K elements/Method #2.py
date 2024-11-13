# Python code to demonstrate
# Remove Front K elements
# using negative list slicing

# initializing list
test_list = [1, 4, 6, 3, 5, 8]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using negative list slicing
# Remove Front K elements
res = test_list[-(len(test_list) - K) or None:]

# printing result
print ("The list after removing first K elements : " + str(res))
