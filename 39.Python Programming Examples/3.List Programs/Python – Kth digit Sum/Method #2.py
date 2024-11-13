# Python3 code to demonstrate working of
# Kth digit Sum
# Using sum() + list comprehension + str()

# initializing list
test_list = [5467, 34232, 45456, 22222, 3455]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# sum() getting summation
res = sum([int(str(ele)[K]) for ele in test_list])

# printing result
print("Kth digit sum : " + str(res))
