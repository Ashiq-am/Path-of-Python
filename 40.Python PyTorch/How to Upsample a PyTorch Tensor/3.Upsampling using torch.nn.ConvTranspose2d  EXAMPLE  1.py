import torch

# create a random input tensor
x = torch.rand(1, 3, 2, 4)

# define the transposed convolution layer
transposed_conv = torch.nn.ConvTranspose2d(in_channels=3,
										out_channels=3,
										kernel_size=3,
										stride=2,
										padding=1,
										output_padding=1)

# apply the transposed convolution layer
y = transposed_conv(x)

# print the input and output tensor shapes
print("Input tensor shape: ", x.shape)
print("Output tensor shape: ", y.shape)
