import pandas as pd
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
         'Sub-Category': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
         'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
         'Values': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Group the data and aggregate
grouped = df.groupby(['Category', 'Sub-Category', 'Region'])['Values'].sum()

# Convert the Series to a DataFrame using unstack
df_converted = grouped.unstack(['Sub-Category', 'Region'])
print(df_converted)
