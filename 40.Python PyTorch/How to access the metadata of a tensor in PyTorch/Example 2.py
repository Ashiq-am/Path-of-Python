# Python Program demonstrate how to
# access meta-data of a Tensor

# Import the library
import torch

# Creating a tensor
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tensor = torch.tensor(data)

# Printing tensor
print(tensor)

# Get the meta-data of tensor
# Get the size of tensor
tensor_size = tensor.size()
print("The size of tensor:\n", tensor_size)

# Applying .shape method to get the tensor size
print("The shape of tensor:\n", tensor.shape)

# Compute the number of elements in the tensor
size = torch.numel(tensor)
print("Total number of elements in tensor:\n", size)
