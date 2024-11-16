import pandas as pd

# Read the Excel file
df = pd.read_excel('excel1.xlsx')

# Copy rows based on condition
condition = df['Salary'] > 50000
result = df[condition]

# Save the result to a new Excel file
result.to_excel('excel2.xlsx', index=False)
