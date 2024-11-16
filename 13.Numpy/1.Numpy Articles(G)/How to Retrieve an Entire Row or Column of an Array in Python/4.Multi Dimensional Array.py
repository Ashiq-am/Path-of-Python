# importing the required package
import numpy as np

# creating a numpy integer array
mat1 = np.array([[1, 2, 3, 4], [4, 5, 6, 8], [7, 6, 8, 9]])
print("Original matrix ")
print(mat1)

print("Row from 1st to 2nd index")
print(mat1[1:3])

# 1st columns
print("Last three columns")

# prints all the columns till the end
print(mat1[:, 1:])

# printing a subset of matrix
print("Matrix subset")
# row index 1 and 2 inclusive and col_index 2 and 3 inclusive
print(mat1[1:3, 2:4])
