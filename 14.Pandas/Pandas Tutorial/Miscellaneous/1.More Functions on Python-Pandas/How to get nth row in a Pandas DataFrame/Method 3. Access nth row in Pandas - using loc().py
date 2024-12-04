import pandas as pd

# Create a DataFrame with custom indices
data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data, index=['x', 'y', 'z'])

# Access row with index 'y'
row = df.loc['y']
print(row)