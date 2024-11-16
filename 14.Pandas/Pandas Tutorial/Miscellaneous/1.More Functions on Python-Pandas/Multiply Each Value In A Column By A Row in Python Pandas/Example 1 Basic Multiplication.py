import pandas as pd

# Create DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Create Row for Multiplication
row = pd.Series([10, 20, 30], index=['A', 'B', 'C'])

# Multiply Column by Row
result = df.mul(row, axis=1)

print("Original DataFrame:\n", df)
print("Row for Multiplication:\n", row)
print("Resulting DataFrame:\n", result)

# This code is contributed by Susobhan Akhuli
