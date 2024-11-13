# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.00001, -5.699, 7.100001, 10.0001])
print(a)

# Applying the ceil function and
# storing the result in 'out'
out = torch.ceil(a)
print(out)
