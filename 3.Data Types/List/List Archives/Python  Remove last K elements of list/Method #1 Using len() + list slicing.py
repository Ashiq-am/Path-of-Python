# Python code to demonstrate
# remove last K elements
# using len() + list slicing

# initializing list
test_list = [1, 4, 6, 3, 5, 8]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using len() + list slicing
# remove last K elements
res = test_list[: len(test_list) - K]

# printing result
print ("The list after removing last K elements : " + str(res))
