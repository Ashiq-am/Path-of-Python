# import torch
import torch

# Define two 2D tensors
tens_1 = torch.Tensor([[10, 20], [30, 40]])
tens_2 = torch.Tensor([[1, 2], [3, 4]])

# display tensors
print(" First tensor: ", tens_1)
print(" Second tensor: ", tens_2)

# Multiply above two 2-D tensors
tens = torch.mul(tens_1, tens_2)
print(" After multiply 2D tensors: ", tens)
