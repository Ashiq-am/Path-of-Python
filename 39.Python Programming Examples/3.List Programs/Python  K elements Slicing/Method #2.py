# Python code to demonstrate
# K elements Slicing
# using negative list slicing

# initializing list
test_list = [1, 4, 6, 3, 5, 8]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using negative list slicing
# K elements Slicing
res = test_list[ : -(len(test_list) - K)]

# printing result
print ("The K sliced List : " + str(res))
