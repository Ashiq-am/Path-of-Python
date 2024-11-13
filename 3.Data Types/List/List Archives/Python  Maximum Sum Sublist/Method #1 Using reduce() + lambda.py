# Python code to demonstrate
# maximum sum sublist
# using reduce() + lambda

# importing functools for reduce()
import functools

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using reduce() + lambda
# maximum sum sublist
res = functools.reduce(lambda i, j: i if sum(i) > sum(j)
	else j, test_matrix)

# printing result
print ("Maximum sum sublist is : " + str(res))
