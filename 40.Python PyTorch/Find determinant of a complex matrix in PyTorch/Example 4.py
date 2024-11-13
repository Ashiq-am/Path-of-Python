# import library
import torch

# create matrix
mat = torch.randn(3,2,2, dtype = torch.cfloat)

# display matrix
print("Batch of Complex Matrices: \n", mat)

# Compute the determinant
det = torch.linalg.det(mat)
print("Determinant: \n", det)
