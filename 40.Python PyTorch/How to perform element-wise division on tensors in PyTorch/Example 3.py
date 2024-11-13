# Python program to divide a 3D tensor by
# a 1D tensor element-wise
# Importing torch
import torch

# defining tensors
a = torch.randn(3, 2, 2)
b = torch.randn(2)

# printing the matrices
print("Tensor a :\n", a)
print("\nTensor b :\n", b)

# divide tensor a by b
result = torch.div(a, b)
print("\nElementwise Division Output :\n", result)
