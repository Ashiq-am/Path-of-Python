# import pandas lib as pd
import pandas as pd

# read both 1st and 2nd sheet.
df = pd.read_excel('SampleWork.xlsx', na_values = "Mssing",
										sheet_name =[0, 1])

print(df)
