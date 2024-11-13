# importing torch
import torch

# define the dividend
tens_1 = torch.tensor([[16., -12.],
					[-10., 30.], ])
print("\n\n Dividend: \n", tens_1)

# define the divisor
tens_2 = torch.tensor([[5., -6.],
					[5., 8.], ])

print("\n Divisor: \n", tens_2)

# compute the remainder using fmod()
remainder = torch.fmod(tens_1, tens_2)

# display result
print("\n Remainder:\n", remainder)
