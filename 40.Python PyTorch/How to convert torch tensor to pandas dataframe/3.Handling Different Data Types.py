import torch
import pandas as pd

# Create a PyTorch tensor with mixed data types
tensor = torch.tensor([[1, 2.5], [3, 4.8]], dtype=torch.float32)

# Convert the tensor to a NumPy array
numpy_array = tensor.detach().numpy()

# Create a Pandas DataFrame from the NumPy array
df = pd.DataFrame(numpy_array, columns=['Integers', 'Floats'])

print(df)
