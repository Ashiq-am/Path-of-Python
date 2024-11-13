import torch
import numpy as np

# Set the seed to 42
torch.manual_seed(42)
# Generate a random tensor
random_tensor = torch.rand(5)
print("Random Pytorch Tensor:",random_tensor)

# Set the seed to 42
np.random.seed(42)
# Generate a random array
random_array = np.random.rand(5)
print("Random Numpy Array:",random_array)
