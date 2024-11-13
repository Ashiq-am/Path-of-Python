import torch
import numpy as np

# Generate a 1D tensor of size 5 filled with random numbers
random_tensor = torch.rand(5)
print('PyTorch Tensor')
print(random_tensor)

# Generate a 1D array of 5 random numbers
random_array = np.random.rand(5)
print('Numpy Array')
print(random_array)
