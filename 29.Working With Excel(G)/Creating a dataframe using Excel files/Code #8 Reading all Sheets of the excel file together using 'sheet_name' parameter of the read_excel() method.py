# import pandas lib as pd
import pandas as pd

# read all sheets together.
all_sheets_df = pd.read_excel('SampleWork.xlsx', na_values = "Missing",
													sheet_name = None)

print(all_sheets_df)
