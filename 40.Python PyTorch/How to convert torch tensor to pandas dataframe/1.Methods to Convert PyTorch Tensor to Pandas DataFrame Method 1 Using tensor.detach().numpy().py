import torch
import pandas as pd

# Create a PyTorch tensor
tensor = torch.rand(4, 4)

# Convert the tensor to a NumPy array
numpy_array = tensor.detach().numpy()

# Create a Pandas DataFrame from the NumPy array
df = pd.DataFrame(numpy_array)

print(df)
