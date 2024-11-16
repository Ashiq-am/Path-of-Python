import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],
				'B': [4, 5, 6],
				'C': ['f;', 'd:', 'sda;sd'],
				'D': ['s', 'd;', 'd;p'],
				'E': [5, 3, 6],
				'F': [7, 4, 3]})

print(df)

cols_to_check = ['C', 'D', 'E']
print(df.iloc[[0, 2]])

df.iloc[[0, 2]] = df.iloc[[0, 2]].replace({';': ''}, regex=True)
print(df)
