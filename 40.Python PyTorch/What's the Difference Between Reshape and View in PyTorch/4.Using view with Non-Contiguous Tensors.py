import torch

x = torch.randn(2, 4, 8)
z = x[:, ::2]
try:
    z.view(-1)
except RuntimeError as e:
    print(e)
