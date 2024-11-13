# import torch
import torch

# Define two 2D tensors
tens_1 = torch.Tensor([[10, 20], [30, 40]])
tens_2 = torch.Tensor([2, 4])

# display tensors
print(" 2D tensor: ", tens_1)
print(" 1D tensor: ", tens_2)

# Multiply above two 2-D tensors
tens = torch.mul(tens_1, tens_2)
print(" After multiply tensors: ", tens)
