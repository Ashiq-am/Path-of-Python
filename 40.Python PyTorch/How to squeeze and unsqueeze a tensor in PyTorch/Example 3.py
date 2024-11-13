# Python program to unsqueeze the input tensor

# importing torch
import torch

# define the input tensor
input = torch.arange(8, dtype=torch.float)
print("Input tensor:\n", input)
print("Size of input Tensor before unsqueeze:\n",
	input.size())

output = torch.unsqueeze(input, dim=0)
print("Tensor after unsqueeze with dim=0:\n", output)
print("Size after unsqueeze with dim=0:\n",
	output.size())

output = torch.unsqueeze(input, dim=1)
print("Tensor after unsqueeze with dim=1:\n", output)
print("Size after unsqueeze with dim=1:\n",
	output.size())
