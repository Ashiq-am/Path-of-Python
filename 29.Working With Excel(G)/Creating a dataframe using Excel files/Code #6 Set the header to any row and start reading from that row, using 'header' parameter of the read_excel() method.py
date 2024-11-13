# import pandas lib as pd
import pandas as pd

# setting the 3rd row as header.
df = pd.read_excel('SampleWork.xlsx', sheet_name = 1, header = 2)

print(df)
