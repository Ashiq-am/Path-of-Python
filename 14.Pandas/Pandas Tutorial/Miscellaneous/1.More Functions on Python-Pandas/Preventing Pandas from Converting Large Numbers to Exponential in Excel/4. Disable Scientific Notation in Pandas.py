import pandas as pd

# Disable scientific notation for large numbers
pd.options.display.float_format = '{:.0f}'.format

# Example DataFrame with large numbers
data = {
    'large_number': [123456789012345, 987654321098765]
}
df = pd.DataFrame(data)

# Write to Excel
df.to_excel('output_file.xlsx', index=False)
print(df)
