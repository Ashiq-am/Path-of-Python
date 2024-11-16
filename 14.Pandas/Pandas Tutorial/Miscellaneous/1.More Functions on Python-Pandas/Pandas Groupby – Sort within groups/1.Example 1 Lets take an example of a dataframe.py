df = pd.DataFrame({'X': ['B', 'B', 'A', 'A'],
				'Y': [1, 2, 3, 4]})

# using groupby function
df.groupby('X').sum()
