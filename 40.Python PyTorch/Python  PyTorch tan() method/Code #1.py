# Importing the PyTorch library
import torch

# A constant tensor of size 6
a = torch.FloatTensor([1.0, -0.5, 3.4, -2.1, 0.0, -6.5])
print(a)

# Applying the tan function and
# storing the result in 'b'
b = torch.tan(a)
print(b)
