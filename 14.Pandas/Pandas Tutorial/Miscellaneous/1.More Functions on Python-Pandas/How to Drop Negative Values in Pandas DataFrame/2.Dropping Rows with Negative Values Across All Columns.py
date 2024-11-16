import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, -3, 4, -5],
        'B': [5, -6, 7, 8, 9]}
df = pd.DataFrame(data)

# Method 2: Using applymap and dropna
df_filtered = df.applymap(lambda x: x if x >= 0 else None).dropna()

print("DataFrame after dropping negative values:")
print(df_filtered)
