# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1, 4, 6, 8, 10, 14])
print(a)

# Applying the clamp function and
# storing the result in 'out'
out = torch.clamp(a, min=5, max=10)
print(out)
