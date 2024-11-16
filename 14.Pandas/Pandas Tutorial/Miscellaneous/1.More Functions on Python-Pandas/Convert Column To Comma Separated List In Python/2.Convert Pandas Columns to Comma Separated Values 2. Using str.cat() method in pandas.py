import pandas as pd

# Using the same DataFrame as above
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
		'Age': [25, 30, 22, 35]}
df = pd.DataFrame(data)

# Convert the 'Name' column to a comma-separated list using str.cat()
name_list = df['Name'].str.cat(sep=', ')
print("Comma-separated list of names:", name_list)

# Convert the 'Age' column to a comma-separated list using str.cat()
name_list = df['Age'].astype(str).str.cat(sep=', ')
print("Comma-separated list of names:", name_list)
