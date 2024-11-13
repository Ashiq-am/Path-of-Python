# import torch library
import torch

# define 1D tensor
tens_1 = torch.Tensor([1, 2])

# define 2D tensor
tens_2 = torch.Tensor([[10, 20], [20, 40]])

# display tensors
print("\nFirst Tensor \n", tens_1)
print("\nsecond Tensor \n", tens_2)

# perform addition on tensors
tens = torch.add(tens_1, tens_2)

# display final output
print("\n After Element-wise Addition\n", tens)
