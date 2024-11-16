import pandas as pd
import numpy as np

# Install xlsxwriter
#!pip install xlsxwriter

# Set Pandas display precision to 30 decimal places
pd.set_option('display.precision', 30)

# Example data with high precision
data = {
    'ID': [1, 2, 3],
    'HighPrecisionNumber': [np.pi, np.e, np.sqrt(2)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame to check precision
print(df)

# Export to Excel with high precision
import xlsxwriter # Import the installed module
with pd.ExcelWriter('high_precision_numbers.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Define a format with 30 decimal places
    number_format = workbook.add_format({'num_format': '0.' + '0'*30})

    # Apply the format to the relevant column (B in this case)
    worksheet.set_column('B:B', 30, number_format)
