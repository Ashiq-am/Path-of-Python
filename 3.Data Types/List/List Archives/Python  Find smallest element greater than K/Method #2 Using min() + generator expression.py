# Python3 code to demonstrate
# smallest number greater than K
# using min() + generator expression

# Initializing list
test_list = [1, 4, 7, 5, 10]

# Initializing k
k = 6

# Printing original list
print ("The original list is : " + str(test_list))

# Using min() + generator expression
# to find smallest number
# greater than K
min_val = min(i for i in test_list if i > k)

# Printing result
print ("The minimum value greater than 6 is : " + str(min_val))
