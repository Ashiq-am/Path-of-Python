# import pandas lib as pd
import pandas as pd

# Handling missing values of 3rd sheet of an excel file.
dataframe = pd.read_excel('SampleWork.xlsx', na_values = "Missing",
													sheet_name = 2)

print(dataframe)
