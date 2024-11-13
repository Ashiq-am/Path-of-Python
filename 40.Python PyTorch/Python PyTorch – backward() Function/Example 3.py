# import necessary libraries
import torch

# define two tensors
A = torch.tensor(2., requires_grad=True)
print("Tensor-A:", A)
B = torch.tensor(5., requires_grad=False)
print("Tensor-B:", B)

# define a function using above defined
# tensors
x = A*B
print("x:", x)

# call the backward method
x.backward()

# print the gradients using .grad
print("A.grad:", A.grad)
print("B.grad:", B.grad)
