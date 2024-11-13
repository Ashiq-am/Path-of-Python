# Import the required libraries
import torch
from numpy import pi

# define a complex tensor
input = torch.tensor([[1 - 2j, 2 + 3j, 3 - 3j],
					[4 + 3j, 5 - 4j, -6 + 2j],
					[-7 - 2j, 8 + 2j, 9 - 4j]])

# print the above define tensor
print("\n Input Tensor:\n ", input)

# compute the elements-wise angle in radians
radians = torch.angle(input)

# print the computed elements-wise angle in radians
print("\n Elements-wise angles in radians:\n ", radians)

# convert the angle in degree
degree = radians * 180/pi

# print the computed elements-wise angle in degree
print("\n Elements-wise angles in degree:\n ", degree)
