# Importing the PyTorch library
import torch

# A constant tensor of size n
a = torch.FloatTensor([1, 4, 6, 3])
print(a)

# Applying the exp function and
# storing the result in 'out'
out = torch.exp(a)
print(out)
