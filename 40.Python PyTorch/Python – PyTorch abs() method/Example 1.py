# Importing the PyTorch library
import torch

# A constant tensor of size 1
a = torch.FloatTensor([-15])
print(a)

# Applying the abs function and
# storing the result in 'b'
b = torch.abs(a)
print(b)
