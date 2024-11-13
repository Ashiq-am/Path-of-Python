# Python program to compute Hessian in PyTorch
# importing libraries
import torch
from torch.autograd.functional import hessian

# defining a function
def func(x):
	return (2*x.pow(3) - x.pow(2)).sum()

# defining the input tensor
input = torch.tensor([3.])
print("Input:\n", input)

# computing the hessian
output = hessian(func, input)

# printing the above computed tensor
print("Hessian:\n", output)

# .....New input
input = torch.tensor([2., 3., 4.])
print("Input:\n", input)

# computing the hessian
output = hessian(func, input)

# printing the above computed tensor
print("Hessian:\n", output)

# .....New input
input = torch.tensor([[2., 3.], [4., 7]])
print("Input:\n", input)

# computing the hessian
output = hessian(func, input)

# printing the above computed tensor
print("Hessian:\n", output)
