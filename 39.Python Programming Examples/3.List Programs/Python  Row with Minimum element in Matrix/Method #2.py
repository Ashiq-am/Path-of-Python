# Python3 code to demonstrate
# Row with Minimum element in Matrix
# using min() + key

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [7, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using min() + key
# Row with Minimum element in Matrix
res = min(test_matrix, key = min)

# printing result
print ("Minimum element sublist is : " + str(res))
