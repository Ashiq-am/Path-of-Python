# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([-5.4, 6.6, -7.1099, 4.4567])
print(a)

# Applying the frac function and
# storing the result in 'out'
out = torch.frac(a)
print(out)
