import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset

# Create a pandas DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Convert DataFrame to a NumPy array and then to a PyTorch Tensor
tensor = torch.tensor(df.values)

# Create a TensorDataset and DataLoader
dataset = TensorDataset(tensor)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

for batch in dataloader:
    print(batch)
