import torch

# Create a 2x3 tensor
tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a 1x3 tensor (adjusted from 3x1)
tensor_b = torch.tensor([[10, 20, 30]])  # Shape: (1, 3)

# 1. Broadcasting: Add tensor_a and tensor_b
broadcasted_result = tensor_a + tensor_b  # Now this will work
print(f"Broadcasted Addition Result: \n{broadcasted_result}")

# 2. Matrix Multiplication: Multiply tensor_a and its transpose
matrix_multiplication_result = torch.matmul(tensor_a, tensor_a.T)
print(f"Matrix Multiplication Result (tensor_a * tensor_a^T): \n{matrix_multiplication_result}")
