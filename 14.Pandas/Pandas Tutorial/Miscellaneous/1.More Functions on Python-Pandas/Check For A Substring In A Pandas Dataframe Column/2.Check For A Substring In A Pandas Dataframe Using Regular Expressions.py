import pandas as pd
data = {
	'EmployeeID': [101, 102, 103, 104],
	'Name': ['aman', 'bhavna', 'madhav', 'rohan'],
	'Department': ['HR', 'IT', 'Finance', 'Marketing'],
	'Salary': [60000, 75000, 90000, 65000]
}

df = pd.DataFrame(data)

# regular expression pattern with negative lookahead
pattern = r'ma(?!$)'
df['NameContainsPattern'] = df['Name'].str.contains(pattern, regex=True)
filtered_df = df[df['NameContainsPattern']]
print(filtered_df)
