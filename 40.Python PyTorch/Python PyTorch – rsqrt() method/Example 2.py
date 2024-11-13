# Python program to compute the reciprocal of
# square root of a complex tensor
# importing torch
import torch

# define the input tensor
a = torch.randn(4, dtype=torch.cfloat)

# print the input tensor
print("tensor a:\n", a)

# compute reciprocal square root
result = torch.rsqrt(a)

# print the computed result
print("rsqrt of a:\n", result)
