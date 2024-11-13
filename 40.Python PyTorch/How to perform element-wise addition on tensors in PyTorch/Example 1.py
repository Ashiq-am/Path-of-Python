# import torch library
import torch

# define two tensors
tens_1 = torch.Tensor([10, 20, 30, 40, 50])
tens_2 = torch.Tensor([1, 2, 3, 4, 5])

# display tensors
print("\nFirst Tensor \n", tens_1)
print("\nsecond Tensor \n", tens_2)

# Add both the tensor
tens = torch.add(tens_1, tens_2)
print("\n After Element-wise Addition\n", tens)
