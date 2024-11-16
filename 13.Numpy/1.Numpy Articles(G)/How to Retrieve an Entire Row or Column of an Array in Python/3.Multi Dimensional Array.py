# importing the required package
import numpy as np

# creating a numpy integer array
mat1 = np.array([[1, 2, 3], [4, 5, 6]])

print("Original matrix ")
print(mat1)

print("Row at 0th index")
print(mat1[0])

# 1st columns
print("Column at 1st index")
print(mat1[:, 1])

# computing length of array
print("Column at 2nd index")
print(mat1[:, 2])
