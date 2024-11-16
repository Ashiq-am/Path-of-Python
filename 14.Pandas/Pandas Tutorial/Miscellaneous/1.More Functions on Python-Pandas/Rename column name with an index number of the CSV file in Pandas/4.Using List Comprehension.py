import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
		'Age': [25, 30, 22],
		'Salary': [50000, 60000, 45000]}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Rename columns with index numbers using list comprehension
df.columns = [f'Column_{index}' for index in range(len(df.columns))]

# Display dataset with renamed columns
print("\nDataset with Renamed Columns:")
print(df)
