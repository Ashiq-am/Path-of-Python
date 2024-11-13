# importing torch module
import torch

# create one dimensional tensor
a = torch.Tensor([1, 2, 3, 4, 5])

# display shape
print(a.shape)

# add dimension at 0 position
added = a.unsqueeze(0)

print(added.shape)

# add dimension at 1 position
added = a.unsqueeze(1)

print(added.shape)
