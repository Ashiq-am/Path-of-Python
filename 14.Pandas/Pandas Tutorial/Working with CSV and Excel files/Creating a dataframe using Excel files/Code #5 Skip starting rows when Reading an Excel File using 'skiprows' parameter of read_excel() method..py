# import pandas lib as pd
import pandas as pd

# read 2nd sheet of an excel file after
# skipping starting two rows
df = pd.read_excel('SampleWork.xlsx', sheet_name = 1, skiprows = 2)

print(df)
