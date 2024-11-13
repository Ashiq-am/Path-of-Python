# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatStorage(6)
print(a)

# Applying the is_tensor function and
# storing the result in 'out'
out = torch.is_storage(a)
print(out)
