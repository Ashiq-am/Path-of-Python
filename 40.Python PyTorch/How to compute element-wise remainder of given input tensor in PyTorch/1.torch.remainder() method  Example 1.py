# importing torch
import torch

# define the dividend
tens_1 = torch.tensor([5., -12., 25., -10., 30])
print("Dividend: ", tens_1)

# define the divisor
tens_2 = torch.tensor([5., -5., -6., 5., 8.])
print("Divisor: ", tens_2)

# compute the remainder
remainder = torch.remainder(tens_1, tens_2)

# display result
print("Remainder: ", remainder)
