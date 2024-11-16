import pandas as pd

# Creating a relevant 4-column DataFrame
data = {
	'EmployeeID': [101, 102, 103, 104],
	'Name': ['Aman', 'Bhavna', 'Madhav', 'Rohan'],
	'Department': ['HR', 'IT', 'Finance', 'Marketing'],
	'Salary': [60000, 75000, 90000, 65000]
}

df = pd.DataFrame(data)

# Checking for substring 'av' in the 'Name' column and adding a new column
substring = 'av'
df['NameContainsSubstring'] = df['Name'].apply(lambda x: substring in x)
filtered_df = df[df['NameContainsSubstring']]
print(filtered_df)
