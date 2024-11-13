# import library
import torch

# create 2x2 complex matrix using
# random numbers
mat = torch.randn(2,2, dtype = torch.cfloat)

# display the matrix
print("Complex Matrix: \n", mat)

# Compute the determinant of Matrix
# using torch.linalg.det()
det = torch.linalg.det(mat)
print("Determinant: \n", det)
