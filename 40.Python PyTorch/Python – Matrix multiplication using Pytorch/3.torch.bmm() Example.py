import torch

# 3D matrices
mat_1 = torch.randn(2, 3, 3)
mat_2 = torch.randn(2, 3, 4)

print("matrix A :\n",mat_1)
print("\nmatrix B :\n",mat_2)

print("\nOutput :\n",torch.bmm(mat_1,mat_2))
