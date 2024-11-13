# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.3, -5.6, 7.9, 10.1])
print(a)

# Applying the ceil function and
# storing the result in 'out'
out = torch.ceil(a)
print(out)
