# Python3 code to demonstrate
# K Matrix Initialization
# using list comprehension
# and * operator

# Declaring rows
N = 5

# Declaring columns
M = 4

# initializing K
K = 7

# using list comprehension
# to initializing matrix
res = [ [K for i in range(M)] * N]

# printing result
print("The matrix after initializing with K : " + str(res))
