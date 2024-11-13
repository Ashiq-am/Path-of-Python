# Python3 code to demonstrate working of
# Rear Kth elements
# Using list slicing

# initializing list
test_list = [3, 5, 7, 9, 10, 2, 8, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Rear Kth elements
# Starting slicing from Rear (-1) and extracting all Kth elements
res = test_list[-1::-K]

# printing result
print("Rear Kth elements : " + str(res))
