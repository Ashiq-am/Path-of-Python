# Python3 code to demonstrate
# Cropped list Minimum
# using list slicing + min()

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 2

# using list slicing + min()
# front and rear deletion
res = min(test_list[K : -K])

# printing result
print ("The cropped list minimum is : " + str(res))
