# Python3 code to demonstrate
# maximum sum sublist
# using max() + key

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using max() + key
# maximum sum sublist
res = max(test_matrix, key = sum)

# printing result
print ("Maximum sum sublist is : " + str(res))
