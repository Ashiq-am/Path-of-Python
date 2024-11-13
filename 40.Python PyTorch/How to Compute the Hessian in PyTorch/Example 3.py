# Python program to compute Hessian in PyTorch
# importing libraries
import torch
from torch.autograd.functional import hessian

# defining a function
def func(x, y, z):
	return (2*x.pow(2)*y + x*z.pow(3) - 10).sum()

# defining the inputs
input_x = torch.tensor([1.])
input_y = torch.tensor([2.])
input_z = torch.tensor([3.])

#inputs = (input_x, input_y, input_z)

# compute the hessian
output = hessian(func, (input_x, input_y, input_z))

# printing the above computed hessian
print("Hessian Tensor:\n", output)
