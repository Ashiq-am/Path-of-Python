import pandas as pd

# Sample data (replace with your actual DataFrame)
data = {'Values': [0.5, 1.8, 2.3, 3.1, 4.7, 5.2, 6.3]}
df = pd.DataFrame(data)

# Option 1: Automatic labels (no need for bin_labels)
df['Categories'] = pd.cut(df['Values'], bins=[0, 1, 2, 3, 4, 5, 6, 7], right=False, include_lowest=True)

print(df)
