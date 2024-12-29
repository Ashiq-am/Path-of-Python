import pandas as pd

# Creating 10 DataFrames with different columns
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})
df3 = pd.DataFrame({'A': [9, 10], 'D': [11, 12]})

# List of DataFrames
dfs = [df1, df2, df3]

# List to store DataFrames for concatenation
df_list = []

# Get all columns across the DataFrames
all_columns = list(set(df1.columns).union(set(df2.columns), set(df3.columns)))

# For loop to append DataFrames, reindexing them to the same column set
for df in dfs:
    df = df.reindex(columns=all_columns)  # Reindex with all columns
    df_list.append(df)

# Concatenate all DataFrames
result = pd.concat(df_list, ignore_index=True)

print(result)