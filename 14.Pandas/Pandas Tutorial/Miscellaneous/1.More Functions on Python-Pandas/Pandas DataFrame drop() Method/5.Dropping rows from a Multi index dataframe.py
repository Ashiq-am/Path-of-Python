import pandas as pd
# Create a MultiIndex DataFrame
arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_tuples(list(zip(*arrays)), names=['letter', 'number'])
df = pd.DataFrame({'X': [1, 2, 3, 4],'Y': [5, 6, 7, 8]}, index=index)

df_dropped = df.drop(('B', 'one'))
print("\nDataFrame after dropping ('B', 'one'):")
print(df_dropped)