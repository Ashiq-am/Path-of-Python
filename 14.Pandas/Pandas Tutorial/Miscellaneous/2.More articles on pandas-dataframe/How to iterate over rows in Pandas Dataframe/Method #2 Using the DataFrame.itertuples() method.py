# importing pandas
import pandas as pd

# list of dicts
input_df = [{'name':'Sujeet', 'age':10},
			{'name':'Sameer', 'age':110},
			{'name':'Sumit', 'age':120}]

df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)

print('\nRows iterated using itertuples() : ')
for row in df.itertuples():
	print(getattr(row, 'name'), getattr(row, 'age'))
