# Python program to compute Hessian in PyTorch
# importing libraries
import torch
from torch.autograd.functional import hessian

# defining a function
def func(x, y):
	return (2*x*y.pow(2) + x.pow(3) - 10).sum()

# defining the inputs
input_x = torch.tensor([2.])
input_y = torch.tensor([-3.])
inputs = (input_x, input_y)
print("inputs:\n", inputs)

# compute the hessian
output = hessian(func, inputs)

# printing the above computed hessian
print("Hessian:\n", output)
