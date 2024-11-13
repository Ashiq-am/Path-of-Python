import pandas as pd
import torch

# Create a sample DataFrame with mixed data types
df = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],  # Integer column
    'Feature2': [6.0, 7.0, 8.0, 9.0, 10.0]  # Float column
})

# Convert the DataFrame to a NumPy array
numpy_array = df.to_numpy()

# Convert the NumPy array to a PyTorch tensor with mixed data types
tensor = torch.from_numpy(numpy_array)

print(tensor.dtype)  # Output: torch.float64
