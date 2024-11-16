import pandas as pd

# Read the Excel file
df = pd.read_excel('excel1.xlsx')

# Copy columns based on condition
condition = df['Age'] < 30
result = df.loc[condition, ['Name', 'Age']]

# Save the result to a new Excel file
result.to_excel('excel2.xlsx', index=False)
