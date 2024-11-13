# Creating Tensors from a NumPy array
import numpy as np
import torch

numpy_array = np.array([[1, 2, 3], [4, 5, 6]])
torch_tensor = torch.from_numpy(numpy_array)
print("\nPyTorch Tensor:")
print(torch_tensor)
