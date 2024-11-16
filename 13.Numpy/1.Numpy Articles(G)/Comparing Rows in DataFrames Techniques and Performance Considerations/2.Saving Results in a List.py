import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Convert DataFrame to NumPy array for faster operations
df_array = df.values

# Initialize an empty list to store the results
results = []

# Iterate over each row
for i in range(len(df_array)):
    row_results = np.all(df_array[i] == df_array, axis=1)
    results.append(row_results.tolist())

print("\nResults (Consolidated Example):\n", results)
