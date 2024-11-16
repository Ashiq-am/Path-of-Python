import pandas as pd
# Sample DataFrame
data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
# Looping through rows
for index, row in df.iterrows():
	df.at[index, 'new_column'] = row['old_column'] * 2
print("DataFrame after looping through rows:")
print(df)
