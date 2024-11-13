# import required libraries
import torch

# define a tensor
input_tens = torch.tensor([[-0.9383, -1.4378, 0.5247],
						[0.8787, 0.2248, -1.3348],
						[1.3739, 1.3379, -0.2445]])

print("\n input tensor: \n", input_tens)

# Define the Softmax function
softmax = torch.nn.Softmax(dim=0)

# Apply above defined Softmax function on
# input tensor
output = softmax(input_tens)

# display tensor that containing Softmax values
print("\n tensor that containing Softmax values: \n", output)

# display sum
print("\n sum = ", output.sum())
