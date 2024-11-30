import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [3, 4, 5], 'age': [25, 30, 35]})
df3 = pd.DataFrame({'id': [5, 6, 7], 'city': ['New York', 'Los Angeles', 'Chicago']})

# Merge df1, df2, and df3 on 'id' using an outer join
result = pd.merge(pd.merge(df1, df2, on='id', how='outer'), df3, on='id', how='outer')
result