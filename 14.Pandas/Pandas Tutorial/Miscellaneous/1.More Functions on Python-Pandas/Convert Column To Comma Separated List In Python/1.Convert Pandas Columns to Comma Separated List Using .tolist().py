import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
		'Age': [25, 30, 22, 35]}
df = pd.DataFrame(data)
name_list = df['Name'].values.tolist()
print("Comma-separated list of names:", name_list)

age_list = df['Age'].values.tolist()
print("Comma-separated list of names:", age_list)
