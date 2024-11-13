# import required libraries
import torch

# define a tensor
input_tens = torch.tensor([0.1237, 1.8373,
						-0.2343, -1.8373,
						0.2343])

print(" input tensor: ", input_tens)

# Define the Softmax function
softmax = torch.nn.Softmax(dim=0)

# Apply above defined Softmax function
# on input tensor
output = softmax(input_tens)

# display tensor that containing Softmax values
print(" tensor that containing Softmax values: ",
	output)

# display sum
print(" sum = ", output.sum())
