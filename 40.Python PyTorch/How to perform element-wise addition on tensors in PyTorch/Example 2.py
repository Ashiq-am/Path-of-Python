# import the torch library
import torch

# define 2D tensors
tens_1 = torch.Tensor([[1, 2], [3, 4]])
tens_2 = torch.Tensor([[10, 20], [20, 40]])

# display these tensors
print("First Tensor \n", tens_1)
print("second Tensor \n", tens_2)

# perform addition on these tensors
tens = torch.add(tens_1, tens_2)

# display final result
print("\n After Element-wise Addition\n", tens)
