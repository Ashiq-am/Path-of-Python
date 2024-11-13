# Import the required libraries
import torch

# define a complex tensor
input = torch.tensor([1 - 2j, 2 + 1j, 3 - 2j, -4 + 3j, -5 - 2j])

# print the above define tensor
print("\n Input Tensor: ", input)

# compute the elements-wise angle in radians
ang = torch.angle(input)

# print the computed elements-wise angle in radians
print("\n Elements-wise angles in radian: ", ang)
