# importing the module
import numpy as np

# creating two matrices
p = [[1, 2], [2, 3], [4, 5]]
q = [[4, 5, 1], [6, 7, 2]]
print("Matrix p :")
print(p)
print("Matrix q :")
print(q)

# computing product
result = np.dot(p, q)

# printing the result
print("The matrix multiplication is :")
print(result)
