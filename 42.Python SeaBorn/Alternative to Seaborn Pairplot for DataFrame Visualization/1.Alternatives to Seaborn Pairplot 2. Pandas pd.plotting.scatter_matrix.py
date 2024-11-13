import pandas as pd
from pandas.plotting import scatter_matrix

# Replace 'your_dataset.csv' with the actual file name
# or provide the full path if it's in a different directory
df = pd.read_csv("Iris.csv")

# If the file is in a different directory:
# df = pd.read_csv("/path/to/your/directory/your_dataset.csv")

# Check for possible column names
print(df.columns)

# Adjust column names based on the output above
scatter_matrix(df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']], alpha=0.2, figsize=(10, 10))
