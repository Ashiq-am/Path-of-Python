# import torch module
import torch

# Define an 1D tensor
tens = torch.tensor([10, 20, 30, 40, 50, 60, 70, 80])

# display tensor
print("\n Original 1D Tensor: ", tens)

# resize this tensor into 2x4
tens_1 = tens.reshape([2, 4])
print("\n After Resize this Tensor to 2x4 : \n", tens_1)

# resize this tensor into 4x2
tens_2 = tens.reshape([4, 2])
print("\n After Resize this Tensor to 4x2 : \n", tens_2)
