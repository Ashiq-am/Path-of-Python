import pandas as pd


df = pd.DataFrame({'A': [1, 2, 3],
				'B': [4, 5, 6],
				'C': ['f;', 'd:', 'sda;sd'],
				'D': ['s', 'd;', 'd;p'],
				'E': [5, 3, 6],
				'F': [7, 4, 3]})

print(df)

cols_to_check = ['C', 'D', 'E']
print(df.loc[:, cols_to_check])


df.loc[:, cols_to_check] = df.loc[
:, cols_to_check].replace({';': ''}, regex=True)
print(df)
