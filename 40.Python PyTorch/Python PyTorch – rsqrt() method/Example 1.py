# Python program to compute the reciprocal of
# square root of a tensor
# importing torch
import torch

# define the input tensor
a = torch.tensor([1.2, 0.32, 0., -32.3, 4.])

# print the input tenosr
print("tensor a:\n", a)

# compute reciprocal square root
result = torch.rsqrt(a)

# print the computed result
print("rsqrt of a:\n", result)
