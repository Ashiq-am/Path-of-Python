# Python3 code to demonstrate
# smallest number greater than K
# using min() + filter()

# Initializing list
test_list = [1, 4, 7, 5, 10]

# Initializing k
k = 6

# Printing original list
print ("The original list is : " + str(test_list))

# Using min() + filter()
# to find smallest number
# greater than K
min_val = min(filter(lambda i: i > k, test_list))

# Printing result
print ("The minimum value greater than 6 is : " + str(min_val))
