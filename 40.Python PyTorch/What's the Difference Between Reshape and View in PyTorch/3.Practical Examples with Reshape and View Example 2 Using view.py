import torch

x = torch.randn(2, 4, 8)
viewed_tensor = x.view(-1, 8)
print(viewed_tensor)
