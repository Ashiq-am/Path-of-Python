# import torch module
import torch

# Define an 2D tensor
tens = torch.Tensor([[1, 2, 3], [4, 5, 6],
					[7, 8, 9], [10, 11, 12]])

# display tensor
print(" Original 2D Tensor: \n", tens)

# resize this tensor to 2x6
tens_1 = tens.reshape([2, 6])
print("\n After Resize this Tensor to 2x6 : \n", tens_1)

# resize this tensor into 6x2
tens_2 = tens.reshape([6, 2])
print("\n After Resize this Tensor to 6x2 : \n", tens_2)
