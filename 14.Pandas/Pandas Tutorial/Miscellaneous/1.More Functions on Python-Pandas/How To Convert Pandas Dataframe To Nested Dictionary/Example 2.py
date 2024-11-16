import pandas as pd
data = {'Person': ['Alice', 'Bob', 'Alice', 'Bob'],
				'Location': ['Home', 'Work', 'Home', 'Work'],
				'Activity': ['Cooking', 'Meeting', 'Reading', 'Working'],
				'Duration': [30, 60, 45, 120]}

df = pd.DataFrame(data)
nested_dict_another = df.groupby(['Person', 'Location']).apply(lambda x: x[['Activity', 'Duration']].to_dict(orient='records')).to_dict()
print(nested_dict_another)
