# import torch library
import torch

# define tensors
tens_1 = torch.Tensor([[11, 12, 13], [14, 15, 16]])
tens_2 = torch.Tensor([[17, 18, 19], [20, 21, 22]])

# print first tensors
print("tens_1 \n", tens_1)

# print second tensor
print("tens_2 \n", tens_2)

# call torch,cat() function
# join tensor in -1 dimension
tens = torch.cat((tens_1, tens_2), -1)
print("join tensors in the -1 dimension \n", tens)

# join tensor in 0 dimension
tens = torch.cat((tens_1, tens_2), 0)
print("join tensors in the 0 dimension \n", tens)
