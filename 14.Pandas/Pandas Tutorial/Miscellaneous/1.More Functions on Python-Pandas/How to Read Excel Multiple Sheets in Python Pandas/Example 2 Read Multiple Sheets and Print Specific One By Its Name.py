# Importing necessary libraries
import pandas as pd

# Reading multiple sheets from an Excel file
sheets_dict = pd.read_excel('file.xlsx', engine="openpyxl", sheet_name=None)

# Accessing a specific sheet by name
specific_sheet = sheets_dict['Sheet1']
print("Contents of 'Sheet1':\n", specific_sheet)
