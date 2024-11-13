# Python code to demonstrate
# Row with Maximum Product
# using reduce() + lambda

# getting Product
from functools import reduce


def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using reduce() + lambda
# Row with Maximum Product
res = reduce(lambda i, j: i if prod(i) > prod(j) else j, test_matrix)

# printing result
print ("Maximum Product row is : " + str(res))
