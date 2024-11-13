# Python3 program to demonstrate torch.log2() method
# for 2D tensors
# importing torch
import torch

# defining a 2D torch tensor with numbers sampled
# from the discrete uniform distribution
t = torch.empty((3, 4), dtype=torch.float32).random_(1, 50)
print('Tensor:\n', t)

# computing the logarithm base 2 of t
result = torch.log2(t)
print('Logarithm of Tensor:\n', result)
