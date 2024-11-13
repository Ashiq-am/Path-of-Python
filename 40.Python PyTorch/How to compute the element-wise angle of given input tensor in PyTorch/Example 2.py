# Import the required libraries
import torch
from numpy import pi

# define a complex tensor
input = torch.tensor([1 - 2j, 2 + 1j, 3 - 2j, -4 + 3j, -5 - 2j])

# print the above define tensor
print("\n\nInput Tensor: ", input)

# compute the elements-wise angle in radians
ang = torch.angle(input)

# convert the angle in degree
deg = ang*180/pi

# print the computed elements-wise angle in degree
print("\nElements-wise angles in degree: ", deg)
