# import library
import torch

# Create first tensor
first = torch.Tensor([4.4, 2.4, -9.1,
					-5.31, 5.3])

# Create second tensor
second = torch.Tensor([4.4, 5.5, -9.1,
					-5.31, 43])

# print first tensors
print("First Tensor:", first)

# print first tensors
print("Second Tensor:", second)

# Compare element wise tensors
# first and second
print(torch.eq(first, second))
