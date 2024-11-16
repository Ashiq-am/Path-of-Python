# Pivot table
pivot = df.pivot(columns='FRUITS',
				values=['PRICE', 'QUANTITY'])
print(pivot)
