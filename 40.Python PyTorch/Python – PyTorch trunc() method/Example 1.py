# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.randn(6)
print(a)

# Applying the trunc function and
# storing the result in 'out'
out = torch.trunc(a)
print(out)
