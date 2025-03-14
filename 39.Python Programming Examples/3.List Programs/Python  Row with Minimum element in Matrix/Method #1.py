# Python code to demonstrate
# Row with Minimum element in Matrix
# using reduce() + lambda

# initializing matrix
from functools import reduce

test_matrix = [[1, 3, 1], [4, 5, 3], [7, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using reduce() + lambda
# Row with Minimum element in Matrix
res = reduce(lambda i, j: i if min(i) < min(j) else j, test_matrix)

# printing result
print ("Minimum element sublist is : " + str(res))
