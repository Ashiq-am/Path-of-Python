# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.randn(6)
print(a)

# Applying the clamp function and
# storing the result in 'out'
out = torch.clamp(a, min=0.5, max=0.9)
print(out)
