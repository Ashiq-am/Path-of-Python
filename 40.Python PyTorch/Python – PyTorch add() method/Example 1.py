# Importing the PyTorch library
import torch

# A constant tensor of size 6
a = torch.randn(6)
print(a)

# Applying the add function and
# storing the result in 'b'
b = torch.add(a, 5)
print(b)
