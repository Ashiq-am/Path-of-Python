# Python3 code to demonstrate working of
# Adding N to Kth tuple element
# Using list comprehension

# Initializing list
test_list = [(4, 5, 6), (7, 4, 2), (9, 10, 11)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing N
N = 3

# Initializing K
K = 1

# Adding N to Kth tuple element
# Using list comprehension
res = [(a, b + N, c) for a, b, c in test_list]

# printing result
print("The tuple after adding N to Kth element : " + str(res))
