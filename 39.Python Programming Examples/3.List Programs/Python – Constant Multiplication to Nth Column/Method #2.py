# Python3 code to demonstrate working of
# Constant Multiplication to Nth Column
# Using list comprehension

# Initializing list
test_list = [(4, 5, 6), (7, 4, 2), (9, 10, 11)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing N
N = 1

# Initializing K
K = 3

# Constant Multiplication to Nth Column
# Using list comprehension
res = [(a, b * K, c) for a, b, c in test_list]

# printing result
print("The tuple after multiplying K to Nth element : " + str(res))
