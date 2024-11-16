import pandas as pd

# First DataFrame with columns 'A', 'B', 'C'
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4],
    'C': [5, 6]
})

# Second DataFrame with columns 'C', 'B', 'A'
df2 = pd.DataFrame({
    'C': [7, 8],
    'B': [9, 10],
    'A': [11, 12]
})

# Reorder df2 to match the column order of df1
df2 = df2[['A', 'B', 'C']]

# Append with consistent column order
df_appended = pd.concat([df1, df2], ignore_index=True)
print(df_appended)
