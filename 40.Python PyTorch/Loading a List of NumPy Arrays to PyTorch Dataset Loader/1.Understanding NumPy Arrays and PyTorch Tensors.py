import numpy as np
import torch

# Convert NumPy array to PyTorch tensor
np_array = np.array([[1, 2], [3, 4]])
torch_tensor = torch.from_numpy(np_array)

# Convert PyTorch tensor to NumPy array
np_array_back = torch_tensor.numpy()
