import torch
import pandas as pd

# Create a PyTorch tensor
tensor = torch.rand(4, 4)

# Directly convert the tensor to a Pandas DataFrame
df = pd.DataFrame(tensor)

print(df)
