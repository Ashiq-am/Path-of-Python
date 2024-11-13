# import required library
import torch

# define some tensors
tens_1 = torch.Tensor([1, 2, 3])
tens_2 = torch.Tensor([4, 5, 6])
tens_3 = torch.Tensor([7, 8, 9])

# display tensors
print("First Tensor :\n", tens_1)
print("\nSecond Tensor :\n", tens_2)
print("\nThird Tensor :\n", tens_3)

# join tensors in the 0 dimension
tens = torch.stack((tens_1, tens_2, tens_3), 0)
print("\n join tensors in the 0 dimension \n", tens)

# join tensors in the -1 dimension
tens = torch.stack((tens_1, tens_2, tens_3), -1)
print("\n join tensors in the -1 dimension \n", tens)
