import pandas as pd

# Example data
data = {
    'ID': [1, 2, 3],
    'LargeNumber': [12345678901234567890, 98765432109876543210, 19283746556473829101]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert large numbers to strings
df['LargeNumber'] = df['LargeNumber'].astype(str)

# Export to Excel
df.to_excel('large_numbers_as_text.xlsx', index=False)

print(df)
