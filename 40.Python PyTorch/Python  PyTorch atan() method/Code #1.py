# Importing the PyTorch library
import torch

# A constant tensor of size 6
a = torch.FloatTensor([1.0, -0.5, 3.4, 0.2, 0.0, -2])
print(a)

# Applying the inverse tan function and
# storing the result in 'b'
b = torch.atan(a)
print(b)
