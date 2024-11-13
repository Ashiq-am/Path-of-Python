# import required library
import torch

# create two tensors
tens_1 = torch.tensor([11, 0])


# display the tensors
print("\n Input Tensor 1: \n", tens_1)

# compute the logical NOT
tens = torch.logical_not(tens_1)

# display result
print("\n After Compute Logical NOT: \n", tens)
