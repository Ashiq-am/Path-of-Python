import pandas as pd
data = {
	'EmployeeID': [101, 102, 103, 104],
	'Name': ['Aman', 'Bhavna', 'Madhav', 'Rohan'],
	'Department': ['HR', 'IT', 'Finance', 'Marketing'],
	'Salary': [60000, 75000, 90000, 65000]
}

df = pd.DataFrame(data)

# Checking for substring
substring = 'Finance'
df['NameContainsSubstring'] = [substring in Department for Department in df['Department']]
filtered_df = df[df['NameContainsSubstring']]
print(filtered_df)
