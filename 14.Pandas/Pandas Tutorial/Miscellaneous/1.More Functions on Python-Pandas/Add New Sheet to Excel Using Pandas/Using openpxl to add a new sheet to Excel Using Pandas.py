import pandas as pd
from openpyxl import load_workbook

# Generating workbook and writer engine
excel_workbook = load_workbook("xl_file.xlsx")
writer = pd.ExcelWriter("xl_file.xlsx", engine='openpyxl')
writer.book = excel_workbook

# Creating dataframes with different values
data_1 = {'Column1': [11, 22, 33], 'Column2': ['value11', 'value22', 'value33']}
data_2 = {'A': [111, 222, 333], 'B': ['X', 'Y', 'Z']}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# Adding dataframes to Excel as new sheets
df_1.to_excel(writer, sheet_name='Sheet1', index=False)
df_2.to_excel(writer, sheet_name='Sheet2', index=False)

# Saving changes and closing writer
writer.save()
writer.close()
