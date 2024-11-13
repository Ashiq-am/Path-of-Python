# Import the required library
import torch

# create two tensors
tens_1 = torch.tensor([[10, 0], [0, 20]])
tens_2 = torch.tensor([[0, 30], [0, 40]])

# display the tensors
print("Input Tensor 1: \n", tens_1)
print("Input Tensor 2: \n", tens_2)

# compute the logical AND
tens = torch.logical_and(tens_1, tens_2)

# print result
print("After Compute Logical AND: \n", tens)
