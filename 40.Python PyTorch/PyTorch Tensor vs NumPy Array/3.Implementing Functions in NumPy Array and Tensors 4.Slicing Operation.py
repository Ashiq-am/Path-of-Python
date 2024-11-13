import torch
import numpy as np

# Create 2D tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Pytorch Tensor:',tensor)
# Slice the tensor to extract the sub-tensor
sub_tensor = tensor[1:, :2]
print("Tensor after the slicing")
print(sub_tensor)

# Create 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('NumPy Array:',arr)
# Slice the array to extract a subarray
sub_arr = arr[1:, :2]
print("array after slicing")
print(sub_arr)
