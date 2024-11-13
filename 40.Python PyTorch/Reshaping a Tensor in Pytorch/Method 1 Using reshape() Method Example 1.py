# import torch module
import torch

# create an 1 D etnsor with 8 elements
a = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8])

# display tensor shape
print(a.shape)

# diplay actual tensor
print(a)

# reshape tensor into 4 rows and 2 columns
print(a.reshape([4, 2]))

# display shape of reshaped tensor
print(a.shape)
