# Import the required library
import torch

# create two tensors having boolean values
tens_1 = torch.tensor([True, True, False, False])
tens_2 = torch.tensor([True, False, True, False])

# display the above created tensors
print("Input Tensor 1: ", tens_1)
print("Input Tensor 2: ", tens_2)

# compute the logical AND of input1 and input2
tens = torch.logical_and(tens_1, tens_2)

# print result
print("\nAfter Compute Logical AND: ", tens)
