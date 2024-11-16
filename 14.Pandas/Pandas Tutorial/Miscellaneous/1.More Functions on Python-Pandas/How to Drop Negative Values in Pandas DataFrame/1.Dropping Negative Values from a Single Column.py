import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, -3, 4, -5],
        'B': [5, -6, 7, 8, 9]}
df = pd.DataFrame(data)

# Method 1: Using boolean indexing
df_filtered = df[df >= 0].dropna()

print("DataFrame after dropping negative values:")
print(df_filtered)
