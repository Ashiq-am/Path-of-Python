import pandas as pd

data = [
	{'name': 'Alice', 'age': 25, 'city': 'New York'},
	{'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
	{'name': 'Charlie', 'age': 28, 'city': 'New York'},
	# ... additional dictionaries ...
]

df = pd.DataFrame(data)
filtered_data = df[(df['age'] > 25) & (df['city'] == 'New York')].to_dict('records')
print(filtered_data)
