import torch

# Creating a 1-dimensional tensor
tensor = torch.tensor([4, 5, 6])

# Converting the tensor to a NumPy array
numpy_array = tensor.numpy()

print(numpy_array)
print(type(numpy_array))
