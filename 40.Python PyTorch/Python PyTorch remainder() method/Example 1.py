# Python 3 program to demonstrate the
# torch.remainder() method
# importing torch
import torch

# define the dividend
x = torch.tensor([5, -13, 24, -7, 7])
print("Dividend:", x)

# define the divisor
y = 5
print("Divisor:",y)

# compute the remainder
remainder = torch.remainder(x,y)
print("Remainder:",remainder)
z = -5
print("Divisor:",z)
remainder = torch.remainder(x,z)
print("Remainder:",remainder)
