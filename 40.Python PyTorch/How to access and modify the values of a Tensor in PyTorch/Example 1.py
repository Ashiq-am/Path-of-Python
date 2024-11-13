# Import torch libraries
import torch

# create PyTorch tensor
tens = torch.Tensor([1, 2, 3, 4, 5])

# print tensor
print("Original tensor:", tens)

# access a value by there index
temp = tens[2]
print("value of tens[2]:", temp)


# modify a value.
tens[2] = 10

# print tensor after modify the value
print("After modify the value:", tens)
