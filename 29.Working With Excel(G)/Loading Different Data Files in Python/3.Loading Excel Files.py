import pandas as pd
file_path = 'excel.xlsx'

data = pd.read_excel(file_path)
print(data.head())
