# import torch module
import torch

# Define a 2D tensor
tens = torch.tensor([[10, 20, 30],
					[40, 50, 60],
					[70, 80, 90]])

# display original tensor
print("\n Original Tensor: \n", tens)

# find transpose
tens_transpose = torch.transpose(tens, 0, 1)
print("\n Tensor After Transpose: \n", tens_transpose)
