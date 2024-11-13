# import necessary libraries
import torch

# define a tensor
A = torch.tensor(5., requires_grad=True)
print("Tensor-A:", A)

# define a function using above defined
# tensor
x = A**3
print("x:", x)

# call the backward method
x.backward()

# print the gradient using .grad
print("A.grad:", A.grad)
