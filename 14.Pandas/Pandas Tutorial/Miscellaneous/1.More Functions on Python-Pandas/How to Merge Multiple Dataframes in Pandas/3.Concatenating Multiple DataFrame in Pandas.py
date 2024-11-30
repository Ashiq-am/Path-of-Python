import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})
df3 = pd.DataFrame({'A': [9, 10], 'D': [11, 12]})

# Concatenate the DataFrames along rows (axis=0) with an outer join and ignore the index
result = pd.concat([df1, df2, df3], axis=0, join='outer', ignore_index=True)
print(result)