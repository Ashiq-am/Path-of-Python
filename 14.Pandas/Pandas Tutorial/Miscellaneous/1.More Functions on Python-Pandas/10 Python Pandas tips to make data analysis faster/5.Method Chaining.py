# Sample data
data = {
	'column1': [1, 2, None, 4, 5],
	'column2': ['A', 'B', 'C', 'D', 'E']
}
# Without method chaining
df = pd.DataFrame(data)
df = df.dropna(subset=['column1'])
df = df.rename(columns={'column2': 'new_column'})
df = df.reset_index(drop=True)
print("DataFrame without method chaining:")
print(df)
