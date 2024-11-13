# import torch module
import torch

# Define an 1D tensor
tens = torch.Tensor([11, 12, 13, 14, 15, 16, 17, 18])

# display tensor
print("\n Original 2D Tensor: \n", tens)

# resize the tensor to 4 tensors.
# each tensor with 4 rows and 5 columns
tens_1 = tens.resize_(4, 4, 5)
print("\n After resize tensor: \n", tens_1)
