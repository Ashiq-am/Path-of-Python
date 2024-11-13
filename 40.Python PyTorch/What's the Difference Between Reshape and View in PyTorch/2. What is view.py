import torch

x = torch.randn(4, 4)
viewed_tensor = x.view(16)
print(viewed_tensor)
