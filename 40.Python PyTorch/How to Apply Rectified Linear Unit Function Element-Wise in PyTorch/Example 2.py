# Import the required library
import torch
import torch.nn as nn

# define a tensor
input = torch.tensor([[-2., 3., -6., 2.],
					[3., -6., 5., 0.],
					[6., -3., 0., -11.],
					[13., -13., 14., 15.]])

print(" Original Tensor: ", input)

# Apply Rectified Linear Unit Function
# Element-Wise Do this operation
# in-place
Rel = torch.nn.ReLU(inplace=True)
Output = Rel(input)

# display result
print(" Output Tensor: ", Output)
