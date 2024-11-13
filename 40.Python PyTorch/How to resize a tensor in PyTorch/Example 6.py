# import torch library
import torch

# define a tensor
tens = torch.Tensor([10, 20, 30, 40, 50])

# display tensor and it's size
print("\n Original Tensor: ", tens)

# Squeeze the tensor in dimension 1
tens_1 = torch.unsqueeze(tens, dim=1)
print("\n After resize tensor to 5x1: \n", tens_1)
