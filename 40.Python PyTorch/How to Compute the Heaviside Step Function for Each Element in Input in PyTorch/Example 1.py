# Import the required libraries
import torch

# define two tensors
input_tens = torch.tensor([0.3, -1.2, 0, 2.0, 0.9])
values_tens = torch.tensor([0.2])

# display above defined tensors
print(" The Input Tensor: ", input_tens)
print(" The Values Tensor: ", values_tens)

# compute heaviside step function for each
# element
hea = torch.heaviside(input_tens, values_tens)

# Display Output
print(" computed Heaviside step function for each element: \n", hea)
