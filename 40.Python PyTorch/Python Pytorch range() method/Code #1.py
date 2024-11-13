# Importing the PyTorch library
import torch

# Applying the range function and
# storing the resulting tensor in 't'
a = torch.range(1, 6)
print("a = ", a)

b = torch.range(1, 5, 0.5)
print("b = ", b)
