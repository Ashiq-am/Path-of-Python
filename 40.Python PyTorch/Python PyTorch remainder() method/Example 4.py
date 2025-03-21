# Python 3 program to demonstrate the
# torch.remainder() method
# importing torch
import torch
import numpy as np

# define the dividend
x = torch.tensor([15., -13., 0., -15., 0])
print("Dividend:", x)

# define the divisor
y = torch.tensor([0., np.inf, 0., 0., np.inf])
print("Divisor:",y)

# compute the remainder
remainder = torch.remainder(x,y)
print("Remainder:",remainder)
