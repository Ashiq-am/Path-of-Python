import torch

a = torch.arange(4.)
reshaped_tensor = torch.reshape(a, (2, 2))
print(reshaped_tensor)
