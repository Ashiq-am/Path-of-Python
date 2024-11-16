import pandas as pd
df = pd.DataFrame({
    'a': [1, 1, 3],
    'b': [4.0, 5.5, 6.0],
    'c': [7, 8, 9],
    'name': ['hello', 'hello', 'foo']
})

# Group by columns a and name
gb = df.groupby(['a', 'name'])

# Calculate the median
median_result = gb.median().reset_index()

print(median_result)
