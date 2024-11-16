import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
		'Age': [25, 30, 35],
		'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Convert DataFrame to nested JSON
json_data = df.to_json(orient='records')
print(json_data)
