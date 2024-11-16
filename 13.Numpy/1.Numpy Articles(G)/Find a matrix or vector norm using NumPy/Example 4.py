# import library
import numpy as np

# initialze vector
vec = np.arange(9)

# convert vector into matrix
mat = vec.reshape((3, 3))

# compute norm of vector
vec_norm = np.linalg.norm(vec)

print("Vector norm:")
print(vec_norm)

# computer norm of matrix
mat_norm = np.linalg.norm(mat)

print("Matrix norm:")
print(mat_norm)
