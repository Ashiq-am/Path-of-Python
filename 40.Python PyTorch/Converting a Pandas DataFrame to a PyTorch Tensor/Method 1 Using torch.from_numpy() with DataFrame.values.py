import pandas as pd
import torch

# Create a pandas DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Convert DataFrame to a NumPy array and then to a PyTorch Tensor
tensor = torch.from_numpy(df.values)
print(tensor)
