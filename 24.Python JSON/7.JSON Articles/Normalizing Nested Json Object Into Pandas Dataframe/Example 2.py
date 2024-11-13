import json

# Load data from 'complex_data.json'
with open('complex_data.json') as f:
	data = json.load(f)

# Use pd.json_normalize to convert the JSON to a DataFrame
df = pd.json_normalize(data)

# Display the DataFrame
print(df)
