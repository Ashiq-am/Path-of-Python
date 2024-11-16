import pandas as pd

# Import the excel file and call it xls_file
excel_file = pd.ExcelFile('pandasEx.xlsx')

# View the excel_file's sheet names
print(excel_file.sheet_names)

# Load the excel_file's Sheet1 as a dataframe
df = excel_file.parse('Sheet1')
print(df)
