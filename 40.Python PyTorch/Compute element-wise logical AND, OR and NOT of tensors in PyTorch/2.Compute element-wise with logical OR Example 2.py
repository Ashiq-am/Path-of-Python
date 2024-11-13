# Import the required library
import torch

# create two tensors
tens_1 = torch.tensor([[11, 0], [0, 12]])
tens_2 = torch.tensor([[0, 13], [0, 14]])

# display the tensors
print("\n Input Tensor 1: \n", tens_1)
print("\n Input Tensor 2: \n", tens_2)

# compute the logical OR
tens = torch.logical_or(tens_1, tens_2)

# print result
print("\n After Compute Logical OR: \n", tens)
