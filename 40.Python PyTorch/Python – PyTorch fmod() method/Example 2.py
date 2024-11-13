# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([5, 6, 7, 4])
b = torch.FloatTensor([2, 3, 4, 1])
print(a, b)

# Applying the fmod function and
# storing the result in 'out'
out = torch.fmod(a, b)
print(out)
