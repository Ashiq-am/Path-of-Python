# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1, 4, 6, 8])
print(a)

# Applying the numel function and
# storing the result in 'out'
out = torch.numel(a)
print(out)
