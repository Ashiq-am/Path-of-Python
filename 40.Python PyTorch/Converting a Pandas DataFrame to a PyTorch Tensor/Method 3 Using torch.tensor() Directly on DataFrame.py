import pandas as pd
import torch

# Create a pandas DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Directly convert the DataFrame to a Tensor
tensor = torch.tensor(df.to_numpy())
print(tensor)
