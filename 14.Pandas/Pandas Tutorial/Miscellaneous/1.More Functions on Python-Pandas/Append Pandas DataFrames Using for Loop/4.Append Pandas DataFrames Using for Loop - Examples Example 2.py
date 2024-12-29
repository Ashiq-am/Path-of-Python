import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'A': [9, 10], 'B': [11, 12]})

# Append DataFrames to a list
df_list = []
for i in range(1,4):
  df_list.append(eval(f'df{i}'))

# Concatenate all DataFrames in the list
result = pd.concat(df_list, ignore_index=True)

print(result)