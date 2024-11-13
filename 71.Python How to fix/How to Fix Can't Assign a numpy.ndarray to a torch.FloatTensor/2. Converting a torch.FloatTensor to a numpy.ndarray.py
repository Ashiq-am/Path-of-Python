import torch

# Create a PyTorch tensor
torch_tensor = torch.tensor([1.0, 2.0, 3.0])

# Convert the PyTorch tensor to a NumPy array
np_array = torch_tensor.numpy()

print(np_array)
