# Python program to perform element-wise Addition
# import the required library
import torch

# define a tensor
tens_1 = torch.Tensor([1, 2, 3, 4])

# define 2D tensor
tens_2 = torch.Tensor([[10, 20], [30, 40]])

# display tensors
print("\nFirst Tensor \n", tens_1)
print("second Tensor \n", tens_2)

# perform addition on 1D tensors
t1 = torch.add(tens_1, 10)
# display final output
print("\n After adding scalar quantity to 1D tensor: \n", t1)

# perform addition on 2D tensors
t2 = torch.add(tens_2, 20)
# display final output
print("\n After adding scalar quantity to 2D tensor: \n", t2)
