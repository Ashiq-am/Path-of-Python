# import torch module
import torch

# create an 1 D etnsor with 8 elements
a = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8])

# display tensor shape
print(a.shape)

# diplay actual tensor
print(a)

# reshape tensor into 8 rows and 1 column
print(a.reshape([8, 1]))

# display shape
print(a.shape)
