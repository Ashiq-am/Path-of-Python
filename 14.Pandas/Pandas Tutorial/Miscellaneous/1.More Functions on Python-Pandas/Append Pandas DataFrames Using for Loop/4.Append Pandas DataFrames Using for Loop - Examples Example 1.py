import pandas as pd

# Create sample DataFrames with different columns
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

# List of DataFrames to concatenate
dfs = [df1, df2]

# Initialize an empty DataFrame to concatenate into
result = pd.DataFrame()

# For loop to concatenate DataFrames
for df in dfs:
    result = pd.concat([result, df], ignore_index=True, sort=False)

print(result)