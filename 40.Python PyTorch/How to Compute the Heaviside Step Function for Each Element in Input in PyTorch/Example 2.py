# Import the required libraries
import torch

# define a 2D tensor for input
input_tens = input = torch.tensor([[-2.9, 0.0, -1.6, 2.5],
								[0.0, -1.2, 0.0, 0.0],
								[-2.3, 0.0, 1.8, -1.3],
								[0.0, 2.2, -1.3, 0.0]])

# define a tensor for values
values_tens = torch.tensor([0.2, 0.3, 0.4, 0.5])

# display above defined tensors
print("\n\n The Input Tensor: \n", input_tens)
print("\n The Values Tensor: \n", values_tens)

# compute heaviside step function for each
# element
hea = torch.heaviside(input_tens, values_tens)

# Display Output
print("\n computed Heaviside step function for each element: \n", hea)
