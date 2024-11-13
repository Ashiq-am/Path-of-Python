# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1.59, 4.5999, 6.78, 3.99999])
print(a)

# Applying the floor function and
# storing the result in 'out'
out = torch.floor(a)
print(out)
