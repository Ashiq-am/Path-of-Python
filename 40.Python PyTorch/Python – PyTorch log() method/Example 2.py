# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.45, 2.3, 10])
print(a)

# Applying the log function and
# storing the result in 'out'
out = torch.log(a)
print(out)
