# Import the required library
import torch
import torch.nn as nn

# define a tensor
input = torch.tensor([[-1., 0., 2., 0.],
					[3., 4., -5., 0.],
					[6., -9., -10., 11.],
					[0., 13., 14., -15.]])

print(" Original Tensor: ", input)

# Apply Rectified Linear Unit Function
# Element-Wise
Rel = torch.nn.ReLU()
Output = Rel(input)

# display result
print(" Output Tensor: ", Output)
