import torch

# creating Tensors using randn()
mat_1 = torch.randn(2, 3, 3)
mat_2 = torch.randn(3)

# printing the matrices
print("matrix A :\n", mat_1)
print("\nmatrix B :\n", mat_2)

# output
print("\nOutput :\n", torch.matmul(mat_1, mat_2))
