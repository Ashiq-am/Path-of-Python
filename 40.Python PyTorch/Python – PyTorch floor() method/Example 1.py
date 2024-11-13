# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.5, 4.2, 6.7, 3.9])
print(a)

# Applying the floor function and
# storing the result in 'out'
out = torch.floor(a)
print(out)
