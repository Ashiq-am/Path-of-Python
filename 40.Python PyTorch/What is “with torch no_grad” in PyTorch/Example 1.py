# import necessary libraries
import torch

# define a tensor
A = torch.tensor(1., requires_grad=True)
print("Tensor-A:", A)

# define a function using A tensor
# inside loop
with torch.no_grad():
	B = A + 1
print("B:-", B)

# check gradient
print("B.requires_grad=", B.requires_grad)
