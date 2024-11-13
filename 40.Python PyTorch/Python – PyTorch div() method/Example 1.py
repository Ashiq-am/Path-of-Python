# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1, 4, 6, 8, 10, 14])
print(a)

# Applying the div function and
# storing the result in 'out'
out = torch.div(a, 0.5)
print(out)
