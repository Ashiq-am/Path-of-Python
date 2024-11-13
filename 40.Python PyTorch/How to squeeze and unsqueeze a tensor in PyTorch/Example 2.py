# Python program to squeeze the tensor in
# different dimensions

# importing torch
import torch
# creating the input tensor
input = torch.randn(3,1,2,1,4)
print("Dimension of input tensor:", input.dim())
print("Input tensor Size:\n",input.size())

# squeeze the tensor in dimension 0
output = torch.squeeze(input,dim=0)
print("Size after squeeze with dim=0:\n",
	output.size())

# squeeze the tensor in dimension 0
output = torch.squeeze(input,dim=1)
print("Size after squeeze with dim=1:\n",
	output.size())

# squeeze the tensor in dimension 0
output = torch.squeeze(input,dim=2)
print("Size after squeeze with dim=2:\n",
	output.size())

# squeeze the tensor in dimension 0
output = torch.squeeze(input,dim=3)
print("Size after squeeze with dim=3:\n",
	output.size())

# squeeze the tensor in dimension 0
output = torch.squeeze(input,dim=4)
print("Size after squeeze with dim=4:\n",
	output.size())
# output = torch.squeeze(input,dim=5) # Error
