# importing torch module
import torch

# create two dimensional tensor
a = torch.Tensor([[2,3], [1,2]])

# display shape
print(a.shape)

# add dimension at 0 position
added = a.unsqueeze(0)

print(added.shape)
