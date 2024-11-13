# Python 3 program to demonstrate the
# torch.remainder() method
# importing torch
import torch

# define the dividend
x = torch.tensor([15, -13, 15, -15, 0])
print("Dividend:", x)

# define the divisor
y = torch.tensor([7, 7, -7, -7, 7])
print("Divisor:",y)

# compute the remainder
remainder = torch.remainder(x,y)
print("Remainder:",remainder)
