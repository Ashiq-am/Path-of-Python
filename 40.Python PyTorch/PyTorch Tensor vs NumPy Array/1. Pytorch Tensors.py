import torch
# Create a PyTorch tensor from a Python list
tensor_list = torch.tensor([1, 2, 3, 4, 5])
print("PyTorch Tensor from List:")
print(tensor_list)
# Create a PyTorch tensor of zeros with a specified shape
tensor_zeros = torch.zeros(2, 3)
print("\nPyTorch Tensor of Zeros:")
print(tensor_zeros)
# Perform element-wise operations on PyTorch tensors
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
tensor_sum = tensor_a + tensor_b
print("\nElement-wise Sum of Tensors:")
print(tensor_sum)
