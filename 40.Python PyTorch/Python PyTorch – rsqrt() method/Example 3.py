# Python program to compute the reciprocal of
# square root of a multi-dimensional tensor
# importing torch
import torch

# define the input tensor
a = torch.randn(2, 3, 2)

# print the input tensor
print("tensor a:\n", a)

# compute reciprocal square root
result = torch.rsqrt(a)

# print the computed result
print("rsqrt of a:\n", result)
