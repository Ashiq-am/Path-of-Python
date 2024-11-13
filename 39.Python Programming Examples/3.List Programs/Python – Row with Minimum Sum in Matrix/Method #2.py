# Python3 code to demonstrate
# Minimum Sum row in Matrix
# using min() + key

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using min() + key
# Minimum Sum row in Matrix
res = min(test_matrix, key = sum)

# printing result
print ("Minimum sum row is : " + str(res))
