import pandas as pd
# Sample DataFrame
data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
# Using vectorized operations
df['new_column'] = df['old_column'] * 2
print("\nDataFrame after using vectorized operations:")
print(df)
