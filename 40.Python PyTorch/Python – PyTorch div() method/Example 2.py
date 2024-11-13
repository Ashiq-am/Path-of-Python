# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.randn(6)
print(a)

# Applying the div function and
# storing the result in 'out'
out = torch.div(a, 0.3)
print(out)
