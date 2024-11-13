# Python3 code to demonstrate
# Cropped list Minimum
# using del operator + list slicing + min()

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 2

# using del operator + list slicing + min()
# Cropped list Minimum
del test_list[-K:], test_list[:K]
res = min(test_list)

# printing result
print ("The cropped list minimum is : " + str(res))
