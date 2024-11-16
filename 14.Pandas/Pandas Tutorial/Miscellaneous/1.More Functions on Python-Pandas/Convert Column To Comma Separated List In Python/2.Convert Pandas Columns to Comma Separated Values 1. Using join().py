import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
		'Age': [25, 30, 22, 35]}
df = pd.DataFrame(data)

# Convert the 'Name' column to a comma-separated list
name_list = ', '.join(df['Name'])
print("Comma-separated list of names:", name_list)

# Convert the 'Age' column to a comma-separated list
name_list = ', '.join(df['Age'].astype(str))
print("Comma-separated list of Age:", name_list)
