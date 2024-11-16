import pandas as pd

# Create DataFrame with Missing Values
data = {'A': [1, 2, None], 'B': [4, None, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Create Row for Multiplication
row = pd.Series([10, 20, 30], index=['A', 'B', 'C'])

# Multiply Column by Row and Fill Missing Values
result = df.mul(row, axis=1).fillna(0)

print("Original DataFrame with Missing Values:\n", df)
print("Row for Multiplication:\n", row)
print("Resulting DataFrame with Filled Missing Values:\n", result)

# This code is contributed by Susobhan Akhuli
