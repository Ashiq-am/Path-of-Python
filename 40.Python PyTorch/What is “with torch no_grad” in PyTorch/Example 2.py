# import necessary libraries
import torch

# define tensors
A = torch.tensor(1., requires_grad=False)
print("Tensor-A:", A)
B = torch.tensor(2.2, requires_grad=True)
print("Tensor-B:", B)

# define a function x outside loop and
# check gradient
x = A+B
print("x:-", x)
print("x.requires_grad=", x.requires_grad)

# define a function y inside loop and
# check gradient
with torch.no_grad():
	y = B - A
print("y:-", y)
print("y.requires_grad=", y.requires_grad)
