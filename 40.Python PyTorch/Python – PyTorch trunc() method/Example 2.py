# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.5, 3.9, -6.9, 3.678])
print(a)

# Applying the trunc function and
# storing the result in 'out'
out = torch.trunc(a)
print(out)
