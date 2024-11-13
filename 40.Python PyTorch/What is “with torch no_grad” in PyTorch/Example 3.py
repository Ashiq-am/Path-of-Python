# import necessary libraries
import torch

# define a tensor
A = torch.tensor(5., requires_grad=True)
print("Tensor-A:", A)

# define a function x inside loop and
# check gradient
with torch.no_grad():
	x = A**2
print("x:-", x)
print("x.requires_grad=", x.requires_grad)
