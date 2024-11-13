import torch

# Define the batch size and dimensions
batch_size = 5
M, K, P = 4, 3, 2

# Create random tensors for matrices A and B
A = torch.randn(batch_size, M, K)
B = torch.randn(batch_size, K, P)

# Perform batch matrix multiplication using einsum
C = torch.einsum('bmk,bkp->bmp', A, B)

print(C.shape)  # Output: torch.Size([5, 4, 2])
