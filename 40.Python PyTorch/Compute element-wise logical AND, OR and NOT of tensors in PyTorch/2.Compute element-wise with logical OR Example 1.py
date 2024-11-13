# Import the required library
import torch

# create two tensors
tens_1 = torch.tensor([[10, 0, 20, 0]])
tens_2 = torch.tensor([[0, 30, 40, 0]])

# display the tensors
print("\n Input Tensor 1: ", tens_1)
print("\n Input Tensor 2: ", tens_2)

# compute the logical OR
tens = torch.logical_or(tens_1, tens_2)

# print result
print("\n After Compute Logical OR: ", tens)
