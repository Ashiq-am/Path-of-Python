# import pandas lib as pd
import pandas as pd

require_cols = [0, 3]

# only read specific columns from an excel file
required_df = pd.read_excel('SampleWork2.xlsx', usecols=require_cols)

print(required_df)
