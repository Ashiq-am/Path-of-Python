# Python3 code to demonstrate working of
# Get K initial powers of N
# Using list comprehension + ** operator

# initializing N
N = 4

# printing original list
print("The original N is : " + str(N))

# initializing K
K = 6

# list comprehension provides shorthand for problem
res = [N ** idx for idx in range(0, K)]

# printing result
print("Square values of N till K : " + str(res))
