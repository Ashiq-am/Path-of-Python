# Python3 code to demonstrate
# initializing matrix
# using list comprehension

# Declaring rows
N = 5

# Declaring columns
M = 4

# using list comprehension
# to initializing matrix
res = [ [ 0 for i in range(M) ] for j in range(N) ]

# printing result
print("The matrix after initializing : " + str(res))
