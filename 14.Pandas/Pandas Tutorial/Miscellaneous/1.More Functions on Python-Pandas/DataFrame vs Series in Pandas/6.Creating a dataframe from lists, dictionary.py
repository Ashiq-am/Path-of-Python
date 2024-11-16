import pandas as pd

# Initializing a DataFrame from a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
		'Age': [25, 30, 35],
		'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# Initializing a DataFrame from a list of lists
data = [['John', 25, 'New York'],
		['Alice', 30, 'Los Angeles'],
		['Bob', 35, 'Chicago']]
columns = ['Name', 'Age', 'City']
df = pd.DataFrame(data, columns=columns)
print(df)
