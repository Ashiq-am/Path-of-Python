import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, -3, 4, -5],
        'B': [5, -6, 7, 8, 9]}
df = pd.DataFrame(data)

# Method 3: Using all and dropna
df_filtered = df[df.ge(0).all(1)]

print("DataFrame after dropping rows with negative values:")
print(df_filtered)
