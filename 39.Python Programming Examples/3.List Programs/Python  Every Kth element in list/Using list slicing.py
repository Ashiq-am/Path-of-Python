# Python3 code to demonstrate working of
# Kth element list
# Using list slicing

# initializing list
test_list = [6, 4, 8, 9, 10, 5, 8, 9, 10, 2, 34, 5]

# printing list
print("The original list : " + str(test_list))

# initializing K
K = 3

# Kth element list
# Using list slicing
res = test_list[::K]

# Printing result
print("Kth element list is : " + str(res))
