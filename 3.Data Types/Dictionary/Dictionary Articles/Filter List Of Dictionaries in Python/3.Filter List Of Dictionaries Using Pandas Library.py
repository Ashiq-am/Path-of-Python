import pandas as pd

original_list = [{'name': 'Alice', 'age': 25},
				{'name': 'Bob', 'age': 30},
				{'name': 'Charlie', 'age': 22}]

df = pd.DataFrame(original_list)
filtered_df = df[df['age'] > 25].to_dict(orient='records')

print(filtered_df)
