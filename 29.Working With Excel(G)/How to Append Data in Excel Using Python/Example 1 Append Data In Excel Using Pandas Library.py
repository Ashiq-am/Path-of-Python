import pandas as pd

# Existing Excel file
existing_file = 'excel1.xlsx'

# New data to append
new_data = {'Name': ['Bob'], 'Age': [28], 'Salary': [55000]}
df_new = pd.DataFrame(new_data)

# Read existing data
df_existing = pd.read_excel(existing_file)

# Append new data
df_combined = df_existing.append(df_new, ignore_index=True)

# Save the combined data to Excel
df_combined.to_excel(existing_file, index=False)
