# Python3 code to demonstrate
# Retain K Front and Rear elements
# using del operator + list slicing

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 2

# using del operator + list slicing
# Retain K Front and Rear elements
N = len(test_list)
del test_list[K : N - K]

# printing result
print ("The cropped list is : " + str(test_list))
