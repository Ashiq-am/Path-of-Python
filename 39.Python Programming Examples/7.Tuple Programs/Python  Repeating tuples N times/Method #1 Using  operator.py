# Python3 code to demonstrate working of
# Repeating tuples N times
# using * operator

# initialize tuple
test_tup = (1, 3)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 4

# Repeating tuples N times
# using * operator
res = ((test_tup, ) * N)

# printing result
print("The duplicated tuple elements are : " + str(res))
