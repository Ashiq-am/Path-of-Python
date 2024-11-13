# Python3 code to demonstrate
# Retain K Front and Rear elements
# using list slicing

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 2

# using list slicing
# Retain K Front and Rear elements
res = test_list[: K] + test_list[-K :]

# printing result
print ("The cropped list is : " + str(res))
