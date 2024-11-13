# Python3 code to demonstrate
# Incremental K sized Row Matrix Initialization
# using list comprehension

# Initialization of row size
K = 3

# Incremental K sized Row Matrix Initialization
# using list comprehension
res = [[i, i + 1, i + 2] for i in range(1, 10, K)]

# printing result
print ("The Incremental Initialized Matrix is : " + str(res))
