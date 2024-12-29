import pandas as pd

# Example DataFrames (Creating 10 DataFrames with simple values)
dfs = [pd.DataFrame({'A': [i, i+1], 'B': [i+2, i+3]}) for i in range(0, 10)]

# Concatenate all DataFrames in the list
result = pd.concat(df_list, ignore_index=False)

print(result)