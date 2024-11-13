# import torch
import torch


# create a tensor with bool type
a = torch.tensor([100, 200, 2, 3, 4], dtype=torch.bool)

# display tensor
print(a)

# display data type
print(a.dtype)

# create a tensor with bool type
a = torch.tensor([0, 0, 0, 1, 2], dtype=torch.bool)

# display tensor
print(a)

# display data type
print(a.dtype)
