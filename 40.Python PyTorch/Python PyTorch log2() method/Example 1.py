# Python3 program to demonstrate torch.log2() method
# importing torch
import torch

# defining a torch tensor
t = torch.tensor([2., 4., 7., 3.])
print('Tensor:', t)

# computing the logarithm base 2 of t
result = torch.log2(t)
print('Logarithm of Tensor:', result)
