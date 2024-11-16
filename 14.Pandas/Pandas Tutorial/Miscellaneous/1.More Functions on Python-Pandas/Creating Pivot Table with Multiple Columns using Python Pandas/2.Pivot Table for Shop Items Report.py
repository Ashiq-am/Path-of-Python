import pandas as pd
data = {
	'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
	'Category': ['A', 'B', 'A', 'B'],
	'Value1': [10, 15, 20, 25],
	'Value2': [30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Create a pivot table with multiple columns with additional parameters
pivot_table = df.pivot_table(
	index='Date',
	columns='Category',
	values=['Value1', 'Value2'],
	aggfunc='sum',
	margins=True,
	margins_name='Total',
	sort=True
)
print(pivot_table)
