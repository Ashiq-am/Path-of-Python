import numpy as np

# initialize tuples
test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cumulative Nested Tuple Column Product
# using numpy.multiply()
res =tuple(tuple(i) for i in np.multiply(test_tup1, test_tup2))

# printing result
print("The resultant tuple after product : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy
