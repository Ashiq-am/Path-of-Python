# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([5, 6, 7, 4])
print(a)

# Applying the log function and
# storing the result in 'out'
out = torch.log(a)
print(out)
