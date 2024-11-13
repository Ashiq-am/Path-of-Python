import pandas as pd
import torch

# Initialize a pandas DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Convert DataFrame directly to a PyTorch Tensor
tensor = torch.tensor(df.values)
print(tensor)
