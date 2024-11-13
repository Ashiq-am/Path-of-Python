# Python3 code to demonstrate working of
# Minimum K records
# Using sorted() + lambda

# Initializing list
test_list = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]

# Initializing K
K = 2

# printing original list
print("The original list is : " + str(test_list))

# Minimum K records
# Using sorted() + lambda
res = sorted(test_list, key = lambda x: x[1])[:K]

# printing result
print("The lowest K records are : " + str(res))
