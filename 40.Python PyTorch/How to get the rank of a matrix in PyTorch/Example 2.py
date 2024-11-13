# import torch module
import torch

# define a batch of matrix
# the below code create 2 matrix of 4x3
Batch = torch.rand(2, 4, 3)

# Display matrices
print("\n Batch of Matrices: ")
print(Batch)

# get ranks of the matrices
r = torch.linalg.matrix_rank(Batch)

# Display Result
print("\n Batch of matrices rank: ")
print(r)
