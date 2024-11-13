# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([15, -5, 3, -2])
print(a)

# Applying the abs function and
# storing the result in 'b'
b = torch.abs(a)
print(b)
