import pandas as pd
data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	'Age': [28, 34, 22, 45, 31],
	'Salary': [60000, 75000, 50000, 90000, 65000],
	'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
}

df = pd.DataFrame(data)
print(df)
