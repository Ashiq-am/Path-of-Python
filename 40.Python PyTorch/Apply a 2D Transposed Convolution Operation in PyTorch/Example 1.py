# Inport the necessary module
import torch
from torch import nn

# Input
Input = torch.tensor([[0.0, 1.0], [2.0, 3.0]])
#Kernel
Kernel = torch.tensor([[4.0, 1.0], [2.0, 3.0]])

# Redefine the shape in 4 dimension
Input = Input.reshape(1, 1, 2, 2)
Kernel = Kernel.reshape(1, 1, 2, 2)

# Transpose convolution Layer
Transpose = nn.ConvTranspose2d(in_channels =1,
							out_channels =1,
							kernel_size=2,
							stride = 2,
							padding=0,
							bias=False)

# Initialize Kernel
Transpose.weight.data = Kernel
# Output value
Transpose(Input)
