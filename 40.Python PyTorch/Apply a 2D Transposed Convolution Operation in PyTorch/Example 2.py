import torch
import torch.nn as nn

# Define input image
input_image = torch.randn(1, 1, 4, 4)
print('Input Shape:',input_image.shape)
# Define kernel size
kernel_size = (3, 3)

# Define stride
stride = (2, 2)

# Define padding
padding = (1, 1)

# Define transposed convolution layer
transposed_conv = nn.ConvTranspose2d(in_channels=1,
									out_channels=1,
									kernel_size=kernel_size,
									stride=stride,
									padding=padding)

# Perform transposed convolution
output = transposed_conv(input_image)

# Display output
print("output \n", output)
print("\n output Shape", output.shape)
