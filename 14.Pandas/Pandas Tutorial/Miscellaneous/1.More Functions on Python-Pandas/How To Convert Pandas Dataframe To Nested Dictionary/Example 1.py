import pandas as pd

# Your DataFrame
data = {'Name': ['Emily', 'David', 'Emily', 'David'],
		'Chain': ['Panera Bread', 'Starbucks', 'Subway', 'Chick-fil-A'],
		'Food': ['soup', 'coffee', 'sandwich', 'grilled chicken'],
		'Healthy': [True, False, True, True]}

df = pd.DataFrame(data)

# Convert DataFrame to nested dictionary
nested_dict = df.groupby('Name').apply(lambda x: x[['Chain', 'Food', 'Healthy']].to_dict(orient='records')).to_dict()

print(nested_dict)
