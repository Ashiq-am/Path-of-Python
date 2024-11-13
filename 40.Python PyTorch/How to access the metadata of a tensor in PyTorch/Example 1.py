# Python Program demonstrate how
# to access meta-data of a Tensor

# Import necessary libraries
import torch

# Create a tensor of having dimensions 5 X 3
tensor = torch.Tensor([[5,1,7],[7,2,9],[4,7,9],
					[8,12,14],[2,4,7]])
print("tensor:\n", tensor)

# Get the meta-data of tensor
# Get the size of tensor
tensor_size = tensor.size()
print("Thee size of tensor:\n", tensor_size)

# Applying .shape method to get the tensor size
print("The shape of tensor:\n", tensor.shape)

# Compute the number of elements in the tensor
size = torch.numel(tensor)
print("Total number of elements in tensor:\n", size)
