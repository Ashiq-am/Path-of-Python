# Importing the PyTorch library
import torch

# Applying the logspace function and
# storing the resulting tensor in 't'
a = torch.logspace(3, 10, 5)
print("a = ", a)

b = torch.logspace(start =-10, end = 10, steps = 5)
print("b = ", b)
