# Values to add
Origin = pd.Series(data=['BH', 'J&K',
						'BH', 'MP',
						'WB', 'WB'])

# Add a column in dataset
df['Origin'] = Origin
print(df)
