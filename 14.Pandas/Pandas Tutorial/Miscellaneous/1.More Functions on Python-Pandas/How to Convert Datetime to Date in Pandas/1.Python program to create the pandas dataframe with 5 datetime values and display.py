# importing pandas module
import pandas as pd

# create pandas DataFrame with one column with five
# datetime values through a dictionary
df = pd.DataFrame({'DateTime': ['2021-01-15 20:02:11',
								'1989-05-24 20:34:11',
								'2020-01-18 14:43:24',
								'2021-01-15 20:02:10',
								'1999-04-04 20:34:11']})

# display
print(df)
