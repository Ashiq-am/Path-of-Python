# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1, 4, 6, 9])
print(a)

# Applying the is_tensor function and
# storing the result in 'out'
out = torch.is_tensor(a)
print(out)
