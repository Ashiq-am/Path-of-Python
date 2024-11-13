# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([5, 6, 7, 4])
print(a)

# Applying the fmod function and
# storing the result in 'out'
out = torch.fmod(a, 3)
print(out)
