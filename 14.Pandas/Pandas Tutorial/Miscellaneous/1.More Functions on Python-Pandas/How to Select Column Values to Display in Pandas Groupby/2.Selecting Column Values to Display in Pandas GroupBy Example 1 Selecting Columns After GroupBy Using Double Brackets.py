import pandas as pd

# Sample data
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value1': [10, 20, 30, 40, 50, 60],
    'Value2': [100, 200, 300, 400, 500, 600]
}

df = pd.DataFrame(data)

# Group by 'Category'
grouped = df.groupby('Category')

# Aggregate the data
aggregated = grouped.agg({'Value1': 'sum', 'Value2': 'mean'})

# Select specific columns to display
selected_columns = aggregated[['Value1', 'Value2']]

print(selected_columns)
