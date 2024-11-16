import pandas as pd

# Sample DataFrame for advanced grouping
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
		'Value1': [10, 15, 8, 12, 5, 9],
		'Value2': [25, 20, 18, 22, 15, 21]}

df = pd.DataFrame(data)

# Group by 'Category' and apply multiple aggregation functions
grouped_df = df.groupby('Category').agg({'Value1': ['sum', 'mean'], 'Value2': 'max'})

# Rename columns for clarity
grouped_df.columns = ['Total_Value1', 'Average_Value1', 'Max_Value2']

print(grouped_df)
