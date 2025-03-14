# import torch library
import torch

# define two tensors
tens_1 = torch.Tensor([1, 2, 3, 4, 5])
tens_2 = torch.Tensor([10, 20, 30, 40, 50])

# display tensors
print(" First Tensor: ", tens_1)
print(" Second Tensor: ", tens_2)

# multiply tensors
tens = torch.mul(tens_1, tens_2)

# display result after perform element wise multiplication
print(" After Element-wise multiplication: ", tens)
