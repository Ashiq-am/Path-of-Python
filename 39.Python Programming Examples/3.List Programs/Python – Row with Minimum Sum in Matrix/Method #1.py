# Python code to demonstrate
# Minimum Sum row in Matrix
# using reduce() + lambda

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using reduce() + lambda
# Minimum Sum row in Matrix
res = reduce(lambda i, j: i if sum(i) < sum(j) else j, test_matrix)

# printing result
print ("Minimum sum row is : " + str(res))
