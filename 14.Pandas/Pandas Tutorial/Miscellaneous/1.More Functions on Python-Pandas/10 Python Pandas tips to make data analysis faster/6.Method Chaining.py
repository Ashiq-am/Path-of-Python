# With method chaining
df = (pd.DataFrame(data)
	.dropna(subset=['column1'])
	.rename(columns={'column2': 'new_column'})
	.reset_index(drop=True))
print("\nDataFrame with method chaining:")
print(df)
