# Python3 code to demonstrate working of
# Conversion to N * N tuple matrix
# using tuple() + generator expression

# initialize tuple
test_tup = ((5, 4), (3, ), (1, 5, 6, 7), (2, 4, 5))

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing dimension
N = 4

# Conversion to N * N tuple matrix
# using tuple() + generator expression
res = tuple(sub + (0, ) * (N-len(sub)) for sub in test_tup)

# printing result
print("Tuple after filling values : " + str(res))
