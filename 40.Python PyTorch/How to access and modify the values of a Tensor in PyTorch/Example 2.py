# Import torch libraries
import torch

# create PyTorch Tensor
tens = torch.Tensor([[1, 2, 3], [4, 5, 6]])

# Print the tensor
print("Original tensor: ", tens)


# Access all values of only second row
# using slicing
a = tens[1]
print("values of only second row: ", a)

# Access all values of only third column
b = tens[:, 2]
print("values of only third column: ", b)

# Access values of second row and first
# two column
c = tens[1, 0:2]
print("values of second row and first two column: ", c)

# Modifying all the values of second row
tens[1] = torch.Tensor([40, 50, 60])
print("After modifying second row: ", tens)

# Modify values of first rows and last
# two column
tens[0, 1:3] = torch.Tensor([20, 30])
print("After modifying first rows and last two column ", tens)
