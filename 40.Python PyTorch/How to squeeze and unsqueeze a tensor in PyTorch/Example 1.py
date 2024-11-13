# Python program to squeeze the tensor
# importing torch
import torch

# creating the input tensor
input = torch.randn(3,1,2,1,4)
# print the input tensaor
print("Input tensor Size:\n",input.size())

# squeeze the tensor
output = torch.squeeze(input)
# print the squeezed tensor
print("Size after squeeze:\n",output.size())
