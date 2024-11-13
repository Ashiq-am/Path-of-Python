# Python program to demonstrate torch.linalg.svd()
# method for a complex-valued matrix
# importing torch
import torch

# creating a complex-valued matrix (2-D tensor)
Mat = torch.randn(3, 2, dtype=torch.cfloat)
# printing the matrix
print("Matrix:\n", Mat)

# computing SVD of the matrix Mat
U, S, VT = torch.linalg.svd(Mat)

# printing U, S, and Vh
print("U:\n", U)
print("Singular Values (S):\n", S)
print("VT:\n", VT)
print("Shape of U, S and VT:\n", U.shape, S.shape, VT.shape)
