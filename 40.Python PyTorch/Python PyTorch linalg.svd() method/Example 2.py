# Python program to demonstrate torch.linalg.svd()
# method for a real-valued matrix with
# full_matrices=False
# importing torch
import torch

# creating a real-valued matrix (2-D tensor)
Mat = torch.rand(3, 4)
# printing the matrix
print("Matrix:\n", Mat)

# computing SVD of the matrix Mat
U, S, VT = torch.linalg.svd(Mat, full_matrices=False)

# printing U, S, and Vh
print("U:\n", U)
print("Singular Values (S):\n", S)
print("VT:\n", VT)
print("Shape of U, S and VT:\n", U.shape, S.shape, VT.shape)
