import pandas as pd
import numpy as np

# Create some example DataFrames
dataframes = [pd.DataFrame(np.random.rand(10, 5)) for _ in range(100)]

# Efficient way: collect in a list and concatenate once
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the result
print(combined_df)