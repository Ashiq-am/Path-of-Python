import torch

# Define the batch size and dimensions
batch_size = 5
M, K, P = 4, 3, 2

# Create random tensors for matrices A and B
A = torch.randn(batch_size, M, K)
B = torch.randn(batch_size, K, P)

# Initialize an empty tensor for the result
C = torch.empty(batch_size, M, P)

# Perform batch matrix multiplication using for-loops
for i in range(batch_size):
    C[i] = torch.matmul(A[i], B[i])

print(C.shape)  # Output: torch.Size([5, 4, 2])
