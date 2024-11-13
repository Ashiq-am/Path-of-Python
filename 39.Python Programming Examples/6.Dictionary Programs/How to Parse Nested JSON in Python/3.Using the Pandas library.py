import pandas as pd
import json

# Sample nested JSON data
nested_json_data = '{"employees": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}'

# Parsing JSON data using pandas
df = pd.json_normalize(json.loads(nested_json_data), 'employees')

# Accessing dataframe columns
names = df['name']
ages = df['age']

# Printing the results
print("Names:", list(names))
print("Ages:", list(ages))
