# Python3 code to demonstrate
# K Matrix Initialization
# using list comprehension

# Declaring rows
N = 5

# Declaring columns
M = 4

# initializing K
K = 7

# using list comprehension
# to initializing matrix
res = [ [ K for i in range(N) ] for j in range(M) ]

# printing result
print("The matrix after initializing with K : " + str(res))
