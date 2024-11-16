import pandas as pd

data = {
	'EmployeeID': [101, 102, 103, 104],
	'Name': ['Aman', 'Bhavna', 'Madhav', 'Rohan'],
	'Department': ['HR', 'IT', 'Finance', 'Marketing'],
	'Salary': [60000, 75000, 90000, 65000]
}

df = pd.DataFrame(data)

# Checking for substring 'an' in the 'Name' column
substring = 'an'
df['NameContainsSubstring'] = df['Name'].str.contains(substring)
filtered_df = df[df['NameContainsSubstring']]
print(filtered_df)
