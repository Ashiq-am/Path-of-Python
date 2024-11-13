import numpy as np
import torch

# Create a NumPy array
np_array = np.array([1.0, 2.0, 3.0])

# Convert the NumPy array to a PyTorch tensor
torch_tensor = torch.from_numpy(np_array)
torch_float_tensor = torch_tensor.float()

print("PyTorch FloatTensor:", torch_float_tensor)

# Perform some operations on the tensor
torch_float_tensor = torch_float_tensor * 2

# Convert the PyTorch tensor back to a NumPy array
np_array_converted_back = torch_float_tensor.numpy()

print("Converted back to NumPy array:", np_array_converted_back)
