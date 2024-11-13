# import required library
import torch

# define some tensors
tens_1 = torch.Tensor([[1, 2], [3, 4]])
tens_2 = torch.Tensor([[5, 6], [7, 8]])
tens_3 = torch.Tensor([[9, 10], [11, 12]])

# display tensors
print("\n First Tensor :\n", tens_1)
print("\n Second Tensor :\n", tens_2)
print("\n Third Tensor :\n", tens_3)

# Join (stacked) tensors in -1 dimension
tens = torch.stack((tens_1, tens_2, tens_3), -1)
print("\n tensors in -1 dimension \n", tens)

# Join (stacked) tensors in 0 dimension
tens = torch.stack((tens_1, tens_2, tens_3), 0)
print("\n tensors in 0 dimension \n", tens)
