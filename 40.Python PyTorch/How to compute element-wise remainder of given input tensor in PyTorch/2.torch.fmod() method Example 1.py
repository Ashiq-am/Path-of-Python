# importing torch
import torch

# define the dividend
tens_1 = torch.tensor([5., -10., -17., 19., 20.])
print("\n\n Dividend: ", tens_1)

# define the divisor
tens_2 = torch.tensor([2., 5., 17., 7., 10.])

print("\n Divisor: ", tens_2)

# compute the remainder using fmod()
remainder = torch.fmod(tens_1, tens_2)

# display result
print("\n Remainder: ", remainder)
