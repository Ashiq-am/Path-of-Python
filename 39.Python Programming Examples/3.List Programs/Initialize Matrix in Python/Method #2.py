# Python3 code to demonstrate
# initializing matrix
# using list comprehension
# and * operator

# Declaring rows
N = 5

# Declaring columns
M = 4

# using list comprehension
# to initializing matrix
res = [ [0 for i in range(M)]] * N

# printing result
print("The matrix after initializing : " + str(res))
