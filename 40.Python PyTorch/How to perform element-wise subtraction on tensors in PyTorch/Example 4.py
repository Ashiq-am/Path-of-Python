# import torch library
import torch

# define 2D tensor
tens_1 = torch.Tensor([[100, 200], [300, 400]])

# define 1D tensor
tens_2 = torch.Tensor([10, 20])

# display tensors
print("First Tensor:", tens_1)
print("Second Tensor:", tens_2)

# Subtract tensors
tens = torch.sub(tens_1, tens_2)

# display result after perfome element wise subtraction
print("After Element-wise subtraction:", tens)
