import torch
import numpy as np

# Create a 1D tensor
tensor = torch.arange(12)
print('Pytorch Tensor:', tensor)
# Reshape the tensor into 3x4 matrix
reshaped_tensor = tensor.view(3, 4)
print("Reshaped Tensor")
print(reshaped_tensor)

# Create 1D array
arr = np.arange(12)
print('Numpy Array:', arr)
# Reshape the array into 3x4 matrix
reshaped_arr = arr.reshape(3, 4)
print("Reshaped Array")
print(reshaped_arr)
