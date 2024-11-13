import numpy as np
import torch

# Create a NumPy array
np_array = np.array([1.0, 2.0, 3.0])

# Convert the NumPy array to a PyTorch tensor
torch_tensor = torch.from_numpy(np_array)

# If you need a FloatTensor, make sure to convert it to float type
torch_float_tensor = torch_tensor.float()

print(torch_float_tensor)
